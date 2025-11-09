import math
import matplotlib.pyplot as plt
import pandas as pd
import io

# Keep the original show_animation setting
show_animation = True


class AStarPlanner:

    # 1. MODIFIED: Constructor now accepts jet stream parameters
    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y,
                 rc_x=None, rc_y=None, jet_vx=1.0, jet_vy=1.0,
                 J_max_discount=0.5, J_counter_penalty=0.0):

        self.resolution = resolution
        self.rr = rr
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model()
        self.calc_obstacle_map(ox, oy)

        # 2. MODIFIED: Use sets for faster 'in' checks and store jet stream params
        self.fc_x = set(fc_x)
        self.fc_y = set(fc_y)
        self.tc_x = set(tc_x)
        self.tc_y = set(tc_y)

        # Jet stream area (reward zone)
        self.rc_x = set(rc_x) if rc_x is not None else set()
        self.rc_y = set(rc_y) if rc_y is not None else set()

        # Jet stream direction and strength
        self.jet_vx = jet_vx
        self.jet_vy = jet_vy
        self.J_max_discount = J_max_discount      # 0 < J_max_discount <= 1
        self.J_counter_penalty = J_counter_penalty  # >= 0 (optional)

        self.Delta_C1 = 0.3
        self.Delta_C2 = 0.15
        self.costPerGrid = 1


    class Node:
        def __init__(self, x, y, cost, parent_index):
            self.x = x
            self.y = y
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx, sy, gx, gy):

        start_node = self.Node(self.calc_xy_index(sx, self.min_x),
                               self.calc_xy_index(sy, self.min_y), 0.0, -1)
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x),
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict()
        open_set[self.calc_grid_index(start_node)] = start_node

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(self, goal_node,
                                                                     open_set[o]))
            current = open_set[c_id]

            if show_animation:
                plt.plot(self.calc_grid_position(current.x, self.min_x),
                         self.calc_grid_position(current.y, self.min_y), "xc")
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(
                                                 0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            if current.x == goal_node.x and current.y == goal_node.y:
                print(f"Total Trip time required -> {current.cost:.2f}") # Formatted to 2 decimal places
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            del open_set[c_id]

            closed_set[c_id] = current

            for i, _ in enumerate(self.motion):
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * self.costPerGrid, c_id)

                # 3. MODIFIED: Cost calculation logic with jet stream
                # Get grid position once to avoid re-calculation
                gx_pos = self.calc_grid_position(node.x, self.min_x)
                gy_pos = self.calc_grid_position(node.y, self.min_y)

                # Original high-cost area checks
                if gx_pos in self.tc_x and gy_pos in self.tc_y:
                    node.cost += self.Delta_C1 * self.motion[i][2]

                if gx_pos in self.fc_x and gy_pos in self.fc_y:
                    node.cost += self.Delta_C2 * self.motion[i][2]

                # Jet stream reward: discount cost when moving along flow
                if gx_pos in self.rc_x and gy_pos in self.rc_y:
                    # motion direction vector
                    mvx, mvy = float(self.motion[i][0]), float(self.motion[i][1])
                    mv_norm = math.hypot(mvx, mvy)
                    # jet flow vector
                    jvx, jvy = float(self.jet_vx), float(self.jet_vy)
                    jv_norm = math.hypot(jvx, jvy)

                    if mv_norm > 0 and jv_norm > 0:
                        # Cosine of angle between motion and jet stream
                        cos_align = (mvx * jvx + mvy * jvy) / (mv_norm * jv_norm)

                        # align_pos is 1 for perfect alignment, 0 for 90-deg or more
                        align_pos = max(0.0, cos_align)
                        # align_neg is 1 for moving perfectly against, 0 for 90-deg or more
                        align_neg = max(0.0, -cos_align)

                        step_cost = self.motion[i][2] * self.costPerGrid
                        # Apply discount for aligned motion
                        node.cost -= align_pos * self.J_max_discount * step_cost
                        # Optional: apply penalty for counter-flow motion
                        node.cost += align_neg * self.J_counter_penalty * step_cost

                n_id = self.calc_grid_index(node)

                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node
                else:
                    if open_set[n_id].cost > node.cost:
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)

        # MODIFIED: Return the final cost along with the path
        return rx, ry, goal_node.cost

    def calc_final_path(self, goal_node, closed_set):
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)]
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    @staticmethod
    def calc_heuristic(self, n1, n2):
        w = 1.0
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        # Heuristic must not overestimate the cost. A safe bet is to use the lowest possible step cost.
        min_cost = self.costPerGrid * (1.0 - self.J_max_discount)
        d = d * min_cost
        return d

    def calc_heuristic_maldis(n1, n2):
        w = 1.0
        dx = w * math.abs(n1.x - n2.x)
        dy = w * math.abs(n1.y - n2.y)
        return dx + dy

    def calc_grid_position(self, index, min_position):
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x)

    def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False

        # Check for out of bounds index before accessing obstacle_map
        if not (0 <= node.x < self.x_width and 0 <= node.y < self.y_width):
            return False
            
        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
        # print("min_x:", self.min_x)
        # print("min_y:", self.min_y)
        # print("max_x:", self.max_x)
        # print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        # print("x_width:", self.x_width)
        # print("y_width:", self.y_width)

        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)]
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy):
                    d = math.hypot(iox - x, ioy - y)
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True
                        break

    @staticmethod
    def get_motion_model():
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1],
                  [-1, -1, math.sqrt(2)],
                  [-1, 1, math.sqrt(2)],
                  [1, -1, math.sqrt(2)],
                  [1, 1, math.sqrt(2)]]

        return motion

# --- NEW: COST ANALYSIS SECTION ---

def perform_cost_analysis(trip_time):
    """
    Performs cost analysis for different aircraft and scenarios.
    """
    # 1. Define Aircraft Specifications using a pandas DataFrame for clarity
    aircraft_data_csv = """Aircraft,Fuel_Consumption_Rate,Passenger_Capacity,Time_Cost_Low,Time_Cost_Medium,Time_Cost_High,Fixed_Cost
A321neo,54,200,10,15,20,1800
A330-900neo,84,300,15,21,27,2000
A350-900,90,350,20,27,34,2500
"""
    aircraft_df = pd.read_csv(io.StringIO(aircraft_data_csv))
    aircraft_df.set_index('Aircraft', inplace=True)
    
    # Map time cost levels to dataframe columns
    time_cost_map = {
        'low': 'Time_Cost_Low',
        'medium': 'Time_Cost_Medium',
        'high': 'Time_Cost_High'
    }

    # 2. Define Scenarios
    scenarios = {
        "Scenario 1": {"passengers": 3300, "max_flights": 13, "time_cost_level": "medium", "fuel_cost": 0.85},
        "Scenario 2": {"passengers": 1500, "max_flights": 7*4, "time_cost_level": "high", "fuel_cost": 0.96}, # 7 flights/week * 4 weeks/month
        "Scenario 3": {"passengers": 2250, "max_flights": 25, "time_cost_level": "low", "fuel_cost": 0.78}
    }

    print("\n" + "="*50)
    print("       AIRCRAFT COST & SCENARIO ANALYSIS")
    print("="*50)
    print(f"Based on an optimal flight time (T_best) of: {trip_time:.2f} minutes\n")

    # 3. Iterate through each scenario and perform calculations
    for name, params in scenarios.items():
        print(f"\n--- {name.upper()} ---")
        
        results = []
        
        for aircraft_name, specs in aircraft_df.iterrows():
            # Calculate number of flights needed
            flights_needed = math.ceil(params["passengers"] / specs["Passenger_Capacity"])
            
            # Check if the number of flights is feasible
            if flights_needed > params["max_flights"]:
                results.append({
                    "aircraft": aircraft_name,
                    "flights_needed": flights_needed,
                    "total_cost": float('inf'), # Infeasible
                    "cost_per_flight": float('nan'),
                    "feasible": "No"
                })
                continue
            
            # Get parameters for the cost formula
            C_F = params["fuel_cost"]  # Cost of Fuel per kg
            delta_F = specs["Fuel_Consumption_Rate"]  # Fuel consumption rate (kg/min)
            T_best = trip_time
            
            time_cost_column = time_cost_map[params["time_cost_level"]]
            C_T = specs[time_cost_column]  # Time-related cost per minute
            
            C_c = specs["Fixed_Cost"]  # Fixed cost per flight
            
            # Calculate cost for a single flight
            # C = C_F * ΔF * T_best + C_T * T_best + C_c
            cost_per_flight = (C_F * delta_F * T_best) + (C_T * T_best) + C_c
            
            # Calculate total cost for the scenario
            total_cost = cost_per_flight * flights_needed
            
            results.append({
                "aircraft": aircraft_name,
                "flights_needed": flights_needed,
                "total_cost": total_cost,
                "cost_per_flight": cost_per_flight,
                "feasible": "Yes"
            })
            
        # 4. Analyze results and print the recommendation for the current scenario
        best_choice = None
        min_cost = float('inf')
        
        print(f"{'Aircraft':<15} | {'Flights Needed':<15} | {'Feasible?':<10} | {'Total Cost ($)':<20}")
        print("-"*68)
        
        for res in results:
            if res["feasible"] == "Yes":
                cost_str = f"${res['total_cost']:,.2f}"
                if res["total_cost"] < min_cost:
                    min_cost = res["total_cost"]
                    best_choice = res["aircraft"]
            else:
                cost_str = "Exceeds flight limit"
                
            print(f"{res['aircraft']:<15} | {res['flights_needed']:<15} | {res['feasible']:<10} | {cost_str:<20}")
            
        print("-" * 68)
        if best_choice:
            print(f"CONCLUSION: The best aircraft for {name} is the {best_choice} with a total cost of ${min_cost:,.2f}.")
        else:
            print(f"CONCLUSION: No single aircraft model can meet the requirements for {name} within the flight limit.")
        print("="*68)


def main():
    print(__file__ + " start the A star algorithm demo !!")

    # --- SETUP FOR A* PLANNER (Original values) ---
    sx, sy = 0.0, 0.0
    gx, gy = 50.0, 50.0
    grid_size = 1.0
    robot_radius = 1.0

    ox, oy = [], []
    for i in range(-10, 60):
        ox.append(i); oy.append(-10.0)
    for i in range(-10, 60):
        ox.append(60.0); oy.append(i)
    for i in range(-10, 61):
        ox.append(i); oy.append(60.0)
    for i in range(-10, 61):
        ox.append(-10.0); oy.append(i)
    start_x, start_y = 20, 0; end_x, end_y = 25, 20; steps = 425
    for i in range(steps + 1):
        t = i / steps; x = start_x + t * (end_x - start_x); y = start_y + t * (end_y - start_y)
        ox.append(x); oy.append(y)
    start_x, start_y = 10, 55; end_x, end_y = 25, 45; steps = 325
    for i in range(steps + 1):
        t = i / steps; x = start_x + t * (end_x - start_x); y = start_y + t * (end_y - start_y)
        ox.append(x); oy.append(y)
    start_x, start_y = 30, 0; end_x, end_y = 45, 10; steps = 325
    for i in range(steps + 1):
        t = i / steps; x = start_x + t * (end_x - start_x); y = start_y + t * (end_y - start_y)
        ox.append(x); oy.append(y)

    tc_x, tc_y = [], []
    for i in range(10, 26):
        for j in range(20, 46):
            tc_x.append(i); tc_y.append(j)
    fc_x, fc_y = [], []
    for i in range(30, 46):
        for j in range(10, 36):
            fc_x.append(i); fc_y.append(j)

    rc_x, rc_y = [], []
    for i in range(15, 41):
        for j in range(15, 41):
            rc_x.append(i); rc_y.append(j)

    if show_animation:
        plt.plot(ox, oy, ".k")
        plt.plot(sx, sy, "og")
        plt.plot(gx, gy, "xb")
        plt.plot(fc_x, fc_y, "oy")
        plt.plot(tc_x, tc_y, "or")
        plt.plot(rc_x, rc_y, "og", markersize=2, alpha=0.3)
        plt.grid(True)
        plt.axis("equal")

    # Create the planner with jet stream parameters
    a_star = AStarPlanner(ox, oy, grid_size, robot_radius,
                          fc_x, fc_y, tc_x, tc_y,
                          rc_x, rc_y,
                          jet_vx=1.0, jet_vy=1.0,
                          J_max_discount=0.7,
                          J_counter_penalty=0.2)

    # Run the planner and get the path and final time
    rx, ry, final_time = a_star.planning(sx, sy, gx, gy)
    
    # --- RUN THE NEW COST ANALYSIS ---
    if final_time > 0: # Only run analysis if a path was found
        perform_cost_analysis(final_time)
    else:
        print("\nCould not find a path. Cost analysis will be skipped.")

    # --- PLOT THE FINAL PATH ---
    if show_animation:
        plt.plot(rx, ry, "-r")
        plt.pause(0.001)
        plt.show()

if __name__ == '__main__':
    main()
