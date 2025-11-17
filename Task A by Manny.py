"""

A* grid planning

author: Atsushi Sakai(@Atsushi_twi)
        Nikos Kanargias (nkana@tee.gr)

See Wikipedia article (https://en.wikipedia.org/wiki/A*_search_algorithm)

This is the simple code for path planning class

"""



import math

import matplotlib.pyplot as plt

show_animation = True


class AStarPlanner:

    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y):
        """
        Initialize grid map for a star planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.resolution = resolution # get resolution of the grid
        self.rr = rr # robot radis
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model() # motion model for grid search expansion
        self.calc_obstacle_map(ox, oy)

        self.fc_x = fc_x
        self.fc_y = fc_y
        self.tc_x = tc_x
        self.tc_y = tc_y
        

        self.Delta_C1 = 0.3 # cost intensive area 1 modifier
        self.Delta_C2 = 0.15 # cost intensive area 2 modifier

        self.costPerGrid = 1 


    class Node: # definition of a sinle node
        def __init__(self, x, y, cost, parent_index):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx, sy, gx, gy):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """

        start_node = self.Node(self.calc_xy_index(sx, self.min_x), # calculate the index based on given position
                               self.calc_xy_index(sy, self.min_y), 0.0, -1) # set cost zero, set parent index -1
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x), # calculate the index based on given position
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict() # open_set: node not been tranversed yet. closed_set: node have been tranversed already
        open_set[self.calc_grid_index(start_node)] = start_node # node index is the grid index

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(self, goal_node,
                                                                     open_set[
                                                                         o])) # g(n) and h(n): calculate the distance between the goal node and openset
            current = open_set[c_id]

            # show graph
            if show_animation:  # pragma: no cover
                plt.plot(self.calc_grid_position(current.x, self.min_x),
                         self.calc_grid_position(current.y, self.min_y), "xc")
                # for stopping simulation with the esc key.
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(
                                                 0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            # reaching goal
            if current.x == goal_node.x and current.y == goal_node.y:
                print("Total Trip time required -> ",current.cost )
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # print(len(closed_set))

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion): # tranverse the motion matrix
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * self.costPerGrid, c_id)
                
                ## add more cost in cost intensive area 1
                if self.calc_grid_position(node.x, self.min_x) in self.tc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.tc_y:
                        # print("cost intensive area!!")
                        node.cost = node.cost + self.Delta_C1 * self.motion[i][2]
                
                # add more cost in cost intensive area 2
                if self.calc_grid_position(node.x, self.min_x) in self.fc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.fc_y:
                        # print("cost intensive area!!")
                        node.cost = node.cost + self.Delta_C2 * self.motion[i][2]
                    # print()
                
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)
        # print(len(closed_set))
        # print(len(open_set))

        return rx, ry

    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)] # save the goal node as the first point
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    @staticmethod
    def calc_heuristic(self, n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        d = d * self.costPerGrid
        return d
    
    def calc_heuristic_maldis(n1, n2):
        w = 1.0  # weight of heuristic
        dx = w * math.abs(n1.x - n2.x)
        dy = w *math.abs(n1.y - n2.y)
        return dx + dy

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
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

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
        print("min_x:", self.min_x)
        print("min_y:", self.min_y)
        print("max_x:", self.max_x)
        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        print("x_width:", self.x_width)
        print("y_width:", self.y_width)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)] # allocate memory
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x) # grid position calculation (x,y)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy): # Python’s zip() function creates an iterator that will aggregate elements from two or more iterables. 
                    d = math.hypot(iox - x, ioy - y) # The math. hypot() method finds the Euclidean norm
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True # the griid is is occupied by the obstacle
                        break

    @staticmethod
    def get_motion_model(): # the cost of the surrounding 8 points
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1],
                  [-1, -1, math.sqrt(2)],
                  [-1, 1, math.sqrt(2)],
                  [1, -1, math.sqrt(2)],
                  [1, 1, math.sqrt(2)]]

        return motion


def main():
    print(__file__ + " start the A star algorithm demo !!") # print simple notes

    # start and goal position
    sx = 0.0  # [m]
    sy = 0.0  # [m]
    gx = 50.0  # [m]
    gy = 50.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]

    # set obstacle positions for group 8
    # ox, oy = [], []
    # for i in range(-10, 60): # draw the button border 
    #     ox.append(i)
    #     oy.append(-10.0)
    # for i in range(-10, 60):
    #     ox.append(60.0)
    #     oy.append(i)
    # for i in range(-10, 61):
    #     ox.append(i)
    #     oy.append(60.0)
    # for i in range(-10, 61):
    #     ox.append(-10.0)
    #     oy.append(i)
    # for i in range(-10, 40):
    #     ox.append(20.0)
    #     oy.append(i)
    # for i in range(0, 40):
    #     ox.append(40.0)
    #     oy.append(60.0 - i)


    # set obstacle positions for group 9
    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 61): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 61): # draw the left border
        ox.append(-10.0)
        oy.append(i)

    for i in range(100, 260): # draw the free border
        ox.append(i*0.1)
        oy.append((-2/3)*i*0.1+(185/3))

    for i in range(200,260):
        ox.append(i*0.1)
        oy.append(4*i*0.1-80)

    for i in range(300, 460):
        ox.append(i*0.1)
        oy.append((2/3)*i*0.1-20)
    
    # for i in range(40, 45): # draw the button border 
    #     ox.append(i)
    #     oy.append(30.0)


    # set cost intesive area 1
    tc_x, tc_y = [], []
    for i in range(10, 26):
        for j in range(20, 46):
            tc_x.append(i)
            tc_y.append(j)
    
    # set cost intesive area 2
    fc_x, fc_y = [], []
    for i in range(30, 46):
        for j in range(10, 36):
            fc_x.append(i)
            fc_y.append(j)


    if show_animation:  # pragma: no cover
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(sx, sy, "og") # plot the start position 
        plt.plot(gx, gy, "xb") # plot the end position
        
        plt.plot(fc_x, fc_y, "oy") # plot the cost intensive area 1
        plt.plot(tc_x, tc_y, "or") # plot the cost intensive area 2

        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-r") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.show() # show the plot
    
    


if __name__ == '__main__':
    main()

time = 74.52905473706207

def time_status(time_cost_status):
    if time_cost_status == 'low':
        return 2
    elif time_cost_status == 'medium':
        return 3
    else:
        return 4

def costfomula(fuel_cost, trip_fuel, time, time_cost, fixed_cost):
    a = fuel_cost*trip_fuel*time + time_cost*time+fixed_cost
    return a

def flight_count(passengers, passenger_capacity):
    if passengers % passenger_capacity == 0:
        flights = passengers // passenger_capacity
    else:
        flights = (passengers // passenger_capacity) + 1
    return flights

def print_aircraft_name(aircraft_name):
    if aircraft_name == 'a':
        return("A321neo")
    elif aircraft_name == 'b':
        return("A330-900neo")
    else:
        return("A350-900")

def compare_aircraft(total_cost_a, total_cost_b, total_cost_c):
    if total_cost_a < total_cost_b and total_cost_a < total_cost_c:
        return print_aircraft_name('a')
    elif total_cost_b < total_cost_a and total_cost_b < total_cost_c:
        return print_aircraft_name('b')
    else:
        return print_aircraft_name('c')

a = (54.0, 200, 10.0, 15.0, 20.0, 1800)
b = (84.0, 300, 15.0, 21.0, 27.0, 2000)
c = (90.0, 350, 20.0, 27.0, 34.0, 2500)

def scenerio_1():
    passengers = 3300
    maximum_flights = 13
    fuel_cost = 0.85
    time_cost_status = 'medium'
    if flight_count(passengers, a[1]) <= maximum_flights:
        total_cost_a = costfomula(fuel_cost, a[0], time, a[time_status(time_cost_status)], a[5])*flight_count(passengers, a[1])
    else:
        total_cost_a = float('inf')
    
    if flight_count(passengers, b[1]) <= maximum_flights:
        total_cost_b = costfomula(fuel_cost, b[0], time, b[time_status(time_cost_status)], b[5])*flight_count(passengers, b[1])
    else:
        total_cost_b = float('inf')

    if flight_count(passengers, c[1]) <= maximum_flights:
        total_cost_c = costfomula(fuel_cost, c[0], time, c[time_status(time_cost_status)], c[5])*flight_count(passengers, c[1])
    else:
        total_cost_c = float('inf')
    
    
    if total_cost_a == float('inf'):
        print('it is not feasiblt to carry all passengers with A321neo within maximum flights')
    else:
        print('cost of A321neo:', total_cost_a)
    
    if total_cost_b == float('inf'):
        print('it is not feasiblt to carry all passengers with A330-900neo within maximum flights')
    else:
        print('cost of A330-900neo:', total_cost_b)
    
    if total_cost_c == float('inf'):
        print('it is not feasiblt to carry all passengers with A350-900 within maximum flights')
    else:
        print('cost of A350-900:', total_cost_c)
    
    print("The best aircraft of scenario 1 is:", compare_aircraft(total_cost_a, total_cost_b, total_cost_c),)
    
def scenerio_2():
    passengers = 1500
    maximum_flights = float('inf')
    fuel_cost = 0.96
    time_cost_status = 'high'
    if flight_count(passengers, a[1]) <= maximum_flights:
        total_cost_a = costfomula(fuel_cost, a[0], time, a[time_status(time_cost_status)], a[5])*flight_count(passengers, a[1])
    else:
        total_cost_a = float('inf')
    
    if flight_count(passengers, b[1]) <= maximum_flights:
        total_cost_b = costfomula(fuel_cost, b[0], time, b[time_status(time_cost_status)], b[5])*flight_count(passengers, b[1])
    else:
        total_cost_b = float('inf')

    if flight_count(passengers, c[1]) <= maximum_flights:
        total_cost_c = costfomula(fuel_cost, c[0], time, c[time_status(time_cost_status)], c[5])*flight_count(passengers, c[1])
    else:
        total_cost_c = float('inf')
    
    
    if total_cost_a == float('inf'):
        print('it is not feasiblt to carry all passengers with A321neo within maximum flights')
    else:
        print('cost of A321neo:', total_cost_a)
    
    if total_cost_b == float('inf'):
        print('it is not feasiblt to carry all passengers with A330-900neo within maximum flights')
    else:
        print('cost of A330-900neo:', total_cost_b)
    
    if total_cost_c == float('inf'):
        print('it is not feasiblt to carry all passengers with A350-900 within maximum flights')
    else:
        print('cost of A350-900:', total_cost_c)
    
    print("The best aircraft of scenario 2 is:", compare_aircraft(total_cost_a, total_cost_b, total_cost_c),)

def scenerio_3():
    passengers = 2250
    maximum_flights = 25
    fuel_cost = 0.78
    time_cost_status = 'low'
    if flight_count(passengers, a[1]) <= maximum_flights:
        total_cost_a = costfomula(fuel_cost, a[0], time, a[time_status(time_cost_status)], a[5])*flight_count(passengers, a[1])
    else:
        total_cost_a = float('inf')
    
    if flight_count(passengers, b[1]) <= maximum_flights:
        total_cost_b = costfomula(fuel_cost, b[0], time, b[time_status(time_cost_status)], b[5])*flight_count(passengers, b[1])
    else:
        total_cost_b = float('inf')

    if flight_count(passengers, c[1]) <= maximum_flights:
        total_cost_c = costfomula(fuel_cost, c[0], time, c[time_status(time_cost_status)], c[5])*flight_count(passengers, c[1])
    else:
        total_cost_c = float('inf')
    
    
    if total_cost_a == float('inf'):
        print('it is not feasiblt to carry all passengers with A321neo within maximum flights')
    else:
        print('cost of A321neo:', total_cost_a)
    
    if total_cost_b == float('inf'):
        print('it is not feasiblt to carry all passengers with A330-900neo within maximum flights')
    else:
        print('cost of A330-900neo:', total_cost_b)
    
    if total_cost_c == float('inf'):
        print('it is not feasiblt to carry all passengers with A350-900 within maximum flights')
    else:
        print('cost of A350-900:', total_cost_c)
    
    print("The best aircraft of scenario 3 is:", compare_aircraft(total_cost_a, total_cost_b, total_cost_c),)


print("------------------------------------")
scenerio_1()
print("------------------------------------")
scenerio_2()
print("------------------------------------")
scenerio_3()
print("------------------------------------")