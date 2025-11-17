<p align="center">
  <h1 align="center">PolyU AAE1001 Project Group 5 Readme (Five Egg and Toast)</h1>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#1-group-members-and-roles">Group Members and Roles</a>
    </li>
    <li>
      <a href="#2-introduction">Introduction</a>
    </li>
    <li>
      <a href="#3-task-1">Task 1</a>
    </li>
     <li>
      <a href="#4-task-2">Task 2</a>
    </li>
    <li>
      <a href="#5-task-3">Task 3</a>
    </li>
    <li>
      <a href="#6-additional-task-1">Additional Task 1</a>
    </li>
    <li>
      <a href="#7-additional-task-2">Additional Task 2</a>
    </li>
    <li>
      <a href="#8-additional-task-3">Additional Task 3</a>
    </li>
     <li>
      <a href="#9-group-reflections">Group Reflections</a>
    </li>
    <li>
      <a href="#10-presentation-files">Presentation Files</a>
    </li>
    <li>
      <a href="#11-report">Report</a>
    </li>
  </ol>
</details>

<!-- Group Members and Roles -->
## 1. Group Members and Roles
1. Winkelhock, Yau Yue Hong Winkelhock (25034703D)
2. Rodgers, Rodgers Mawalla Maighacho (25094994D)
3. Manny, So Yee Man (25079801D)
4. August, Wang Tiancheng (25095793D)
5. Talia, Cheung Yung Ting Talia (25129573D)
6. Sharon, Chan Chin Ying (25084065D)
7. Sylvia, Lau Tsz Wing (25068927D)

<!-- Introduction -->
## 2. Introduction
### Task Path
### Path Planning

## 3. Task 1
<a href="task1.py"><strong>Task 1 Code</strong></a>
#### Description
#### Calculation Method
#### Scenario 1
#### Scenario 2
#### Scenario 3

### Bonus Part
#### Calculation with Code
#### Cost Function with Manual Calculation
#### Outputs

## 4. Task 2
<a href="task2.py"><strong>Task 2 Code</strong></a>
#### Introducing Jetstream
#### Description
The task involved creating a new cost area that can reduce the cost of the route, based on task 1's code. The aim was to find the best place within the map to set our minus-cost area (jet stream) and reduce the cost by 5%. Similarly, the area of the jet stream had to span across the map laterally and extend 5 units vertically.

#### Setting up with code
Firstly, we performed jet stream initialisation with the AStar Planner Class by modifying it to recognise and use the jet stream parameters; i.e coordinates of the minus cost area, defining the direction of the jet stream and maximum cost reduction.

Then, we established a section that systematically tests every possible vertical placement for the jet stream to find the best placement via the optimisation loop. This was done by iterating every possible vertical start position for the jet stream, then redefining the jet stream area for each iteration to satisfy the lateral span. A new AStar planner is initialised in every loop iteration with the current stream coordinates, and then the 'if current_time<best_time:' function compares the resulting path cost from the current jet stream placement to the running minimum.

The cost calculation logic was then performed via the planning method, whereby the 5% cost reduction was applied to the path search during the A* algorithm. The code checks if the current node is inside the jet stream area, while the discount code reduces the node cost by a maximum of 5% as it is set to 0.05.

Finally, after the loop determines the best time (The lowest cost found), the function shown in the image below takes the optimal time and uses the pandas Dataframe to perform the financial analysis based on scenario 1. 


#### Finalised results
From these, the optimal placement of the jet stream was a vertical span starting (and including) Y=19 to Y=23; satisfying the 5-unit span requirement. This led to an optimal trip time of about 74.18 minutes, as shown in the image below:



## 5. Task 3
<a href="task3.py"><strong>Task 3 Code</strong></a>
#### Introduction
#### Scenarios
#### Calculation

## 6. Additional Task 1
<a href="taska1.py"><strong>Task A1 Code</strong></a>
#### Modified Code
#### Results

## 7. Additional Task 2
<a href="taska2.py"><strong>Task A2 Code</strong></a>
#### Description
#### Results with modified code

## 8. Additional Task 3
<a href="task a3/A star task a3.py"><strong>Task A3 Astar Code</strong></a>

<a href="task a3/Dijkstra task a3.py"><strong>Task A3 Dijkstra Code</strong></a>

<a href="task a3/RRT task a3.py"><strong>Task A3 RRT Code</strong></a>

---
### Introduction of A*, Dijkstra and RRT
---
- **A***

A* was developed in 1968 by Peter Hart, Nils Nilsson, and Bertram Raphael. It is a heuristic-optimized pathfinding algorithm widely used to find the shortest/lowest-cost path between two points.

- **Dijkstra**

The Dijkstra path planning algorithm is a classic algorithm used to find the shortest path between nodes in a graph. Developed by Edsger Dijkstra in 1956, it is widely used in network routing, robotics, and mapping applications.

- **RRT (Rapidly-exploring Random Tree)**

RRT was proposed in 1998 by Steven M. LaValle. It is a widely used method for solving complex motion planning problems, especially in high-dimensional spaces such as robotics and autonomous vehicles.

---
### Theories
---
- **A***

A* is a smart pathfinding algorithm that balances speed and accuracy. Its core is a cost formula: f(n) = g(n) + h(n). Here, g(n) is the exact cost from the start to the current node, and h(n) is a reasonable guess of the cost from the current node to the goal like straight-line distance. It uses two lists to track nodes: one for nodes to explore and one for nodes already checked to avoid repeats. If the guess h(n) never overestimates the real cost, A* guarantees the shortest path. It works best for simple, grid-based environments (e.g., basic flight path planning).

- **Dijkstra**

Dijkstra’s is a straightforward algorithm for finding the shortest path in environments with non-negative costs. It starts by setting the start node’s cost to 0 and all other nodes’ costs to infinity. It then repeatedly picks the node with the lowest current cost, updates the cost of its neighbors (adding the cost of moving between them), and keeps going until it reaches the goal. It doesn’t use any guesses—just explores all nodes in order of increasing cost. This guarantees the shortest path but can be slow for large spaces, as it checks irrelevant nodes too. It’s good for small, weighted graphs (e.g., simple network routing).

- **RRT**

RRT is a probabilistic algorithm designed for complex, high-dimensional environments (e.g., robot arms or drones in 3D space) where grid-based algorithms struggle. It builds a "random tree" to explore the space: it randomly picks a point, finds the closest node in the existing tree, and connects them if the path is obstacle-free. It might prioritize points near the goal to speed up finding a path. RRT doesn’t guarantee the shortest path but is great for unstructured or hard-to-map spaces (e.g., UAV trajectory planning in cluttered areas).

---
### Performance （under task 1 scenario)
---
- **A***

A* balances speed and optimality in the grid: it guarantees the shortest path (using an admissible Euclidean distance heuristic) while focusing exploration toward the goal, reducing unnecessary node checks compared to Dijkstra. It effectively handles cost zones and uses moderate memory (fewer nodes processed than Dijkstra). For the given grid environment, A* is the best all-around choice, suitable for scenarios where both path optimality and efficiency are important.

![astar_animation](https://github.com/user-attachments/assets/917aeeb9-e69d-4b32-ac18-4cd827291ad5)


- **Dijkstra**

Dijkstra's algorithm guarantees the shortest path by exhaustively exploring all possible nodes, expanding the one with the lowest cumulative cost at each step. It accounts for cost zones but is slow in the given grid environment due to its exhaustive search, which checks many nodes. It uses more memory to store all visited nodes. Dijkstra's algorithm is acceptable in this context, but is not the perfect one.

![dijkstra_path](https://github.com/user-attachments/assets/5204791f-852a-4735-8011-6f50e427a238)


- **RRT**

RRT is fast in the provided grid, as it finds a feasible path quickly through random sampling and tree-like expansion, avoiding exhaustive node checks. It handles cost zones but does not guarantee the shortest path—random sampling leads to suboptimal routes. It uses less memory by storing only a tree of nodes. The paths generated by the RRT algorithm in this scenario can vary probabilistically.

![rrt_path](https://github.com/user-attachments/assets/d1e35424-057c-464e-9933-3c5604659317)


---
### Strengths and Limitations
---
#### A*

#### Strengths:
- Efficient with a Good Heuristic: Outperforms Dijkstra’s and BFS in large spaces by focusing exploration on nodes closer to the goal.
- Optimal Path Guarantee: Finds the shortest path if the heuristic is admissible and consistent.
- Goal-Oriented: Prioritizes nodes near the goal, making it highly effective for goal-directed tasks in both weighted and unweighted graphs.

#### Limitations:
- Heuristic-Dependent: Performance relies heavily on the heuristic; a poor or non-admissible heuristic can lead to suboptimal paths or excessive exploration.
- Memory-Intensive: Stores all potential paths and their costs in open/closed sets, which is problematic in extremely large graphs.
- Implementation Complexity: More complex than BFS or Dijkstra’s due to the need for a well-designed heuristic and priority queue management.



#### Djikstra

#### Strengths:
- Guaranteed Optimality: Always finds the shortest path in graphs with non-negative edge weights.
- Simplicity: Easier to implement than A* and has predictable behavior.
- Completeness: Will find a path if one exists.

#### Limitations:
- Slow in Large Spaces: Explores all nodes exhaustively without goal-directed guidance, leading to inefficiency in large or dense graphs.
- High Memory Usage: Stores all visited nodes in memory, which becomes problematic for very large graphs.
- Over-Exploration: Wastes resources on nodes far from the goal, even when a closer path exists.



#### RRT

#### Strengths:
- Efficiency in High-Dimensional Spaces: Excels in large, unstructured, or high-dimensional environments where grid-based algorithms struggle.
- Low Memory Usage: Stores only a tree of sampled nodes, avoiding the need to track all explored space.
- Adaptability to Non-Holonomic Systems: Works well for robots or vehicles with movement constraints.

#### Limitations:
- Non-Optimal Paths: Does not guarantee the shortest path; random sampling often produces suboptimal or jagged routes.
- Probabilistic Completeness: Finds a path with high likelihood if one exists but not with absolute certainty.
- Path Quality Variability: Results depend heavily on parameters like sampling density and iteration count, leading to inconsistent path quality.

### Summarize

<!-- Group Reflections -->
## 9. Group Reflections
Winkelhock, Yau Yue Hong Winkelhock (25034703D)

Rodgers, Rodgers Mawalla Maighacho (25094994D)

August, Wang Tiancheng (25095793D)

Manny, So Yee Man (25079801D)

Talia, Cheung Yung Ting Talia (25129573D)

Sharon, Chan Chin Ying (25084065D)

Sylvia, Lau Tsz Wing (25068927D)

<!-- Presentation Files -->
## 10. Presentation Files

<!-- Report -->
## 11. Report
