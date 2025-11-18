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

#### Description
The task involved creating a new cost area that can reduce the cost of the route, based on task 1's code. The aim was to find the best place within the map to set our minus-cost area (jet stream) and reduce the cost by 5%. Similarly, the area of the jet stream had to span across the map laterally and extend 5 units vertically.

#### Setting up with code
Firstly, we performed jet stream initialisation with the AStar Planner Class by modifying it to recognise and use the jet stream parameters; i.e coordinates of the minus cost area, defining the direction of the jet stream and maximum cost reduction.

<img width="610" height="219" alt="Screenshot 2025-11-17 at 16 52 08" src="https://github.com/user-attachments/assets/dfa9e22e-0f57-419c-ba35-fb4a84d5907c" />

_(An image showing jet stream initialisation, VS Code, Author's own)_

Then, we established a section that systematically tests every possible vertical placement for the jet stream to find the best placement via the optimisation loop. This was done by iterating every possible vertical start position for the jet stream, then redefining the jet stream area for each iteration to satisfy the lateral span. A new AStar planner is initialised in every loop iteration with the current stream coordinates, and then the 'if current_time<best_time:' function compares the resulting path cost from the current jet stream placement to the running minimum.

<img width="688" height="514" alt="Screenshot 2025-11-17 at 16 52 50" src="https://github.com/user-attachments/assets/64602e92-4b78-494f-b49b-7837834e26d3" />

_(An image showing optical loop placement, VS Code, Author's own)_

The cost calculation logic was then performed via the planning method, whereby the 5% cost reduction was applied to the path search during the A* algorithm. The code checks if the current node is inside the jet stream area, while the discount code reduces the node cost by a maximum of 5% as it is set to 0.05.

<img width="712" height="492" alt="Screenshot 2025-11-17 at 16 55 21" src="https://github.com/user-attachments/assets/c51cfc40-daf3-44b5-b832-cedb33965e15" />

_(An image showing the Cost Calculation logic code, VS Code, Author's Own)_


Finally, after the loop determines the best time (i.e., the lowest cost found), the function shown in the image below takes the optimal time. It uses the Pandas DataFrame to perform the financial analysis based on Scenario 1. 

<img width="496" height="394" alt="Screenshot 2025-11-17 at 16 56 59" src="https://github.com/user-attachments/assets/aca8d615-500f-43cc-8acc-024aea5beac0" />

_(An image showing the code performing cost analysis, VS Code, Author's own)_

#### Finalised results
From these, the optimal placement of the jet stream was a vertical span starting (and including) Y=19 to Y=23; satisfying the 5-unit span requirement. This led to an optimal trip time of about 74.18 minutes, as shown in the image below:

<img width="560" height="501" alt="Screenshot 2025-11-17 at 16 48 23" src="https://github.com/user-attachments/assets/5b3a2ec2-17c4-4c58-b793-07c84920ebef" />

_(An image showing optimal jet stream placement as per the parameters, VS Code, Author's own)_

We were also able to compile the bonus code to find the best aircraft based on scenario 1, task 1, as shown below.

<img width="733" height="296" alt="Screenshot 2025-11-17 at 16 49 06" src="https://github.com/user-attachments/assets/f61286e4-983d-4937-8f6d-826e34dd6673" />

_(An image showing final code analysis results, VS Code, Author's own)_

## 5. Task 3
<a href="task3.py"><strong>Task 3 Code</strong></a>
#### Introduction
#### Scenarios
#### Calculation

## 6. Additional Task 1
<a href="taska1.py"><strong>Task A1 Code</strong></a>
# Description 
This task is required modify the code inorder to to add two check points in each cost intensive area,
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
**A***

A* balances speed and optimality in the grid: it guarantees the shortest path (using an admissible Euclidean distance heuristic) while focusing exploration toward the goal, reducing unnecessary node checks compared to Dijkstra. It effectively handles cost zones and uses moderate memory (fewer nodes processed than Dijkstra). For the given grid environment, A* is the best all-around choice, suitable for scenarios where both path optimality and efficiency are important.


![astar_animation](https://github.com/user-attachments/assets/b471356e-3a17-4ac2-aed1-4acca2423925)


**Dijkstra**

Dijkstra's algorithm guarantees the shortest path by exhaustively exploring all possible nodes, expanding the one with the lowest cumulative cost at each step. It accounts for cost zones but is slow in the given grid environment due to its exhaustive search, which checks many nodes. It uses more memory to store all visited nodes. Dijkstra's algorithm is acceptable in this context, but is not the perfect one.


![dijkstra_path](https://github.com/user-attachments/assets/dcc0b2c0-fa4f-4f38-82a4-fe2f77621843)


**RRT**

RRT is fast in the provided grid, as it finds a feasible path quickly through random sampling and tree-like expansion, avoiding exhaustive node checks. It handles cost zones but does not guarantee the shortest path—random sampling leads to suboptimal routes. It uses less memory by storing only a tree of nodes. The paths generated by the RRT algorithm in this scenario can vary probabilistically.


![rrt_path](https://github.com/user-attachments/assets/6431e695-deb6-4fa5-b6c7-eba1d5cae11c)



---
### Strengths and Limitations
---
### A*

#### Strengths:
A* is efficient with a good heuristic, outperforming Dijkstra’s and BFS in large spaces by focusing exploration on nodes closer to the goal; it also guarantees an optimal path if the heuristic is admissible and consistent, and is goal-oriented—prioritizing nodes near the goal to be highly effective for goal-directed tasks in both weighted and unweighted graphs.

#### Limitations:
A* is heuristic-dependent, as its performance relies heavily on the heuristic (a poor or non-admissible heuristic can lead to suboptimal paths or excessive exploration); it is also memory-intensive, storing all potential paths and their costs in open/closed sets, which becomes problematic in extremely large graphs, and has higher implementation complexity than BFS or Dijkstra’s due to the need for a well-designed heuristic and priority queue management.



### Djikstra

#### Strengths:
Dijkstra’s algorithm guarantees optimality by always finding the shortest path in graphs with non-negative edge weights, offers simplicity as it is easier to implement than A* with predictable behavior, and ensures completeness by finding a path if one exists.


#### Limitations:
Dijkstra’s algorithm is slow in large spaces as it explores all nodes exhaustively without goal-directed guidance, leading to inefficiency in large or dense graphs; it has high memory usage due to storing all visited nodes, which becomes problematic for very large graphs, and suffers from over-exploration by wasting resources on nodes far from the goal even when a closer path exists.



### RRT

#### Strengths:
RRT (Rapidly Exploring Random Tree) excels in high-dimensional spaces, outperforming grid-based algorithms in large, unstructured environments; it has low memory usage by storing only a tree of sampled nodes instead of tracking all explored space, and is adaptable to non-holonomic systems, working well for robots or vehicles with movement constraints.

#### Limitations:
RRT does not guarantee optimal paths—random sampling often produces suboptimal or jagged routes; it only achieves probabilistic completeness, finding a path with high likelihood if one exists but not with absolute certainty, and has variable path quality as results depend heavily on parameters like sampling density and iteration count.

---

### Algorithm Comparison Summary

| Algorithm          | Theory                                                                 | Strengths                                                                 | Limitations                                                                 | Performance                                                 |
|--------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| **A\***            | - Uses f(n) = g(n) + h(n) , g(n) = start cost, h(n) = heuristic to goal.<br>- Informed & goal-directed. | - Efficient with good heuristic<br>- Goal-focused<br>- Finds optimal path | - Heuristic-dependent<br>- High memory use<br>- Complex logic               | - Fast (good heuristic)<br>- Slower (poor heuristic)        |
| **Dijkstra**       | - Explores nodes by smallest known distance from source.<br>- Works on non-negative edge-weight graphs. | - Guarantees shortest path<br>- No heuristic needed<br>- Handles non-negative weights | - Explores irrelevant nodes<br>- Not goal-oriented<br>- Heavy memory use    | - Explores many nodes<br>- Slower than A* (good heuristic)  |
| **RRT**            | - Grows random tree from start, samples nodes to reach goal.<br>- Uses collision check for path feasibility. | - Simple to implement<br>- Works in high-dimensional space<br>- Avoids full graph search | - Non-optimal path<br>- Randomness affects efficiency<br>- Slow in cluttered space | - Fast (sparse environments)<br>- Unreliable (narrow passages) |

<!-- Group Reflections -->
## 9. Group Reflections
Winkelhock, Yau Yue Hong Winkelhock (25034703D)

Rodgers, Rodgers Mawalla Maighacho (25094994D)

The group project enabled me to gain numerous collaboration and leadership skills. By overseeing the project, I learnt the positive effect of adhering to mini-deadlines, i.e finishing presentation slides within a weekend and ensuring everyone stays up to date with their tasks. I gained some coding knowledge from the coding leader, through whom I learnt to update our code in GitHub and run it to ensure it satisfies the assessment criteria. Additionally, through the lectures, I was able to acquire skills to be efficient in using AI to modify and correct various code segments, making the work cleaner and easier to interpret, especially for me as a coding beginner. In managing task 2, which involved finding an optimum cost area based on set restraints (5% reduction cost along the jet stream and specific jet stream dimensions), I was able to understand how the AStar planner 


August, Wang Tiancheng (25095793D)

Manny, So Yee Man (25079801D)

Talia, Cheung Yung Ting Talia (25129573D)

Sharon, Chan Chin Ying (25084065D)

Sylvia, Lau Tsz Wing (25068927D)

In this group project, I learned how to use AI effectively to help me in completing tasks. For example, when writing the code, I initially gave a simple instruction to AI, ​​but I found that the results is always wrong, as lots of errors in these codes. After trying few time, I change to asked AI about the meaning of the words in the code. In addition to my understanding, I adjusted the code to achieve the result I wanted. AI also help me to improve my works, gave me ideas which saving my times and allow me to do more things. Moreover, I improved my collaboration and time management skills. Although this group project was not easy, cooperation and mutual assistance among every member made it easier to be complete. Meeting schedules with teammates, meeting deadlines, and breaking up the work into small goals taught me how to prioritize tasks and not rush things at the last minute.

<!-- Presentation Files -->
## 10. Presentation Files

