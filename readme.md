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
### Description
The goal of task 1 is to implements an A path planning algorithm* combined with aircraft selection optimization to find the most cost-effective aircraft for flight routes under various operational constraints. Task 1 focuses on selecting the optimal aircraft model from three available options, including A321neo, A330-900neo, and A350-900 that minimizes total operational cost while satisfying passenger transportation requirements and flight frequency limits. The task can be brought down to the following mini-objectives:

<img width="718" height="541" alt="image" src="https://github.com/user-attachments/assets/9be4a630-8893-4ec6-96e4-8e9c33538f5e" />

Key Objectives:

Path Planning: Use A* algorithm to find the fastest route considering obstacles and cost-intensive areas

Cost Analysis: Evaluate the total operational cost for each aircraft model under different scenarios

Optimization: Determine the best aircraft choice based on minimum cost while meeting constraints

Validation: Compare results across three operational scenarios with varying requirements

Besides, the code has two versions, including human's version and ChatGpt's version. It provide a verification to the result calculated by ChatGpt version.

### Calculation Method

### Cost Formula Overview

The total operational cost per flight is calculated using:

```
C = CF × F × Tbest + CT × Tbest + Cc
```

#### Formula Components

| Symbol | Parameter | Description | Unit |
|--------|-----------|-------------|------|
| **C** | Total Cost | Complete operational cost per flight | $ (dollars) |
| **CF** | Fuel Cost | Cost of fuel per kilogram | $/kg |
| **F** | Fuel Rate | Aircraft fuel consumption rate | kg/min |
| **Tbest** | Trip Time | Optimal flight time from path planning | minutes |
| **CT** | Time Cost | Time-related operational cost per minute | $/min |
| **Cc** | Fixed Cost | Fixed cost independent of time/distance | $ (dollars) |

---

### Total Cost Calculation

| Step | Formula | Description |
|------|---------|-------------|
| **1. Calculate Flights Needed** | `Flights = ⌈Passengers / Capacity⌉` | Round up to nearest whole number |
| **2. Calculate Per-Flight Cost** | `C = CF × F × Tbest + CT × Tbest + Cc` | Use formula above |
| **3. Calculate Total Cost** | `Total = Per-Flight Cost × Flights` | Multiply by number of flights |

---

### Cost-Intensive Area Modifiers

Aircraft routes may pass through special zones that increase operational costs:

| Area Type | Effect | Time Multiplier |
|-----------|--------|-----------------|
| **Time-Consuming Area** | Increases flight time | **+30%** |
| **Fuel-Consuming Area** | Increases flight time | **+15%** |

---

### Movement Rules (Path Planning)

| Movement Type | Time Cost |
|---------------|-----------|
| **Horizontal** | 1 minute |
| **Vertical** | 1 minute |
| **Diagonal** | √2 ≈ 1.414 minutes |

---

### Aircraft Specifications Table

| Aircraft Model | Fuel Rate (kg/min) | Capacity (passengers) | Time Cost - Low ($/min) | Time Cost - Medium ($/min) | Time Cost - High ($/min) | Fixed Cost ($) |
|----------------|--------------------|-----------------------|-------------------------|----------------------------|--------------------------|----------------|
| **A321neo** | 54 | 200 | 10 | 15 | 20 | 1,800 |
| **A330-900neo** | 84 | 300 | 15 | 21 | 27 | 2,000 |
| **A350-900** | 90 | 350 | 20 | 27 | 34 | 2,500 |

---
<img width="445" height="13" alt="image" src="https://github.com/user-attachments/assets/90a76748-3f21-4b69-9bdf-f360318ca768" />

As shown in the table, the best to travel is about 74.53

### Scenario 1

### Scenario Parameters:
- **Passengers**: 3,300
- **Maximum Flights Allowed**: 13 flights per week
- **Time Cost Level**: Medium
- **Fuel Cost**: $0.85 per kg
- **Trip Time (Tbest)**: 74.53 minutes

### Aircraft Evaluation Table:

| Aircraft Model | Fuel Rate (kg/min) | Capacity (passengers) | Flights Required | Fuel Cost per Flight | Time Cost per Flight | Fixed Cost | Per-Flight Cost | Total Cost | Status |
|----------------|--------------------|-----------------------|------------------|----------------------|----------------------|------------|-----------------|------------|--------|
| **A321neo** | 54 | 200 | 17 | — | — | $1,800 | — | — |  **INFEASIBLE** (exceeds 13 flight limit) |
| **A330-900neo** | 84 | 300 | 11 | $5,315.34 | $1,565.13 | $2,000 | $8,880.47 | **$97,685.17** |  **BEST CHOICE** (11 ≤ 13 flights) |
| **A350-900** | 90 | 350 | 10 | $5,708.45 | $2,012.31 | $2,500 | $10,220.76 | $102,207.60 |  **FEASIBLE** (10 ≤ 13 flights) |

### Scenario 1 Result:
** Best Aircraft: A330-900neo**
- **Total Cost**: $97,685.17

### Scenario 2

### Scenario Parameters:
- **Passengers**: 1,500
- **Maximum Flights Allowed**: 7 flights per week
- **Time Cost Level**: High
- **Fuel Cost**: $0.96 per kg
- **Trip Time (Tbest)**: 74.53 minutes

### Aircraft Evaluation Table:

| Aircraft Model | Fuel Rate (kg/min) | Capacity (passengers) | Flights Required | Fuel Cost per Flight | Time Cost per Flight | Fixed Cost | Per-Flight Cost | Total Cost | Status |
|----------------|--------------------|-----------------------|------------------|----------------------|----------------------|------------|-----------------|------------|--------|
| **A321neo** | 54 | 200 | 8 | $3,862.31 | $1,490.60 | $1,800 | $7,152.91 | $57,223.28 |  **INFEASIBLE** (8 > 7 flights) |
| **A330-900neo** | 84 | 300 | 5 | $6,016.43 | $2,012.31 | $2,000 | $10,028.74 | **$50,143.70** |  **BEST CHOICE** (5 ≤ 7 flights) |
| **A350-900** | 90 | 350 | 5 | $6,447.07 | $2,534.02 | $2,500 | $11,481.09 | $57,405.45 |  **FEASIBLE** (5 ≤ 7 flights) |

### Scenario 2 Result:
** Best Aircraft: A330-900neo**
- **Total Cost**: $50,143.70

### Scenario 3

### Scenario Parameters:
- **Passengers**: 2,250
- **Maximum Flights Allowed**: 25 flights per week
- **Time Cost Level**: Low
- **Fuel Cost**: $0.78 per kg
- **Trip Time (Tbest)**: 74.53 minutes

### Aircraft Evaluation Table:

| Aircraft Model | Fuel Rate (kg/min) | Capacity (passengers) | Flights Required | Fuel Cost per Flight | Time Cost per Flight | Fixed Cost | Per-Flight Cost | Total Cost | Status |
|----------------|--------------------|-----------------------|------------------|----------------------|----------------------|------------|-----------------|------------|--------|
| **A321neo** | 54 | 200 | 12 | $3,137.55 | $745.30 | $1,800 | $5,682.85 | $68,194.20 |  **FEASIBLE** (12 ≤ 25 flights) |
| **A330-900neo** | 84 | 300 | 8 | $4,892.63 | $1,117.95 | $2,000 | $8,010.58 | **$64,084.64** |  **BEST CHOICE** (8 ≤ 25 flights) |
| **A350-900** | 90 | 350 | 7 | $5,241.60 | $1,490.60 | $2,500 | $9,232.20 | $64,625.40 |  **FEASIBLE** (7 ≤ 25 flights) |

### Scenario 3 Result:
** Best Aircraft: A330-900neo**
- **Total Cost**: $64,084.64
- **Rationale**: All three aircraft are feasible, but A330-900neo provides the optimal balance between capacity utilization and operational costs, achieving the lowest total cost

### Bonus Part

The bonus part is required that using python find out the best aircraft. The code has been enhanced with automatic cost calculation capabilities that all cost calculations are performed automatically within the program, creating formatted tables for easy comparison. Besides, it can automatically checks if aircraft options are feasible given constraints and compare all feasible options and identifies the minimum-cost choice.

### Calculation with Code

AI Version (task1.py)
The AI version provides a streamlined implementation with integrated cost calculations:
<img width="1495" height="851" alt="image" src="https://github.com/user-attachments/assets/b4d5caf3-ec28-4ff0-af89-11193f70f888" />
<img width="1464" height="430" alt="image" src="https://github.com/user-attachments/assets/41459e5d-f326-40e0-b6f6-0e54bb091d67" />
<img width="602" height="644" alt="image" src="https://github.com/user-attachments/assets/c3c46ad4-78cd-44ce-a68d-ca9bfc1c66d1" />

Manny Version (Task-A-by-Manny.py)
The Manny version demonstrates detailed manual calculation approach
<img width="802" height="657" alt="image" src="https://github.com/user-attachments/assets/85e6b12d-9d69-4bc4-9365-aab3c27e8ede" />

### Comparasion with Ai and human result

Human

<img width="775" height="351" alt="image" src="https://github.com/user-attachments/assets/04accaeb-7e36-4c9e-b192-71b506443321" />

ChatGpt

<img width="928" height="653" alt="image" src="https://github.com/user-attachments/assets/a7c675ee-06a8-4d67-ab83-382993288f0b" />


### Cost Function with Manual Calculation

<img width="802" height="512" alt="image" src="https://github.com/user-attachments/assets/576934ad-de0c-45aa-830e-d8f788e629d7" />

Calculating using Excel

### Outputs
Summary of Results
Key Finding: A330-900neo emerges as the optimal choice across all three scenarios, providing the best balance between operational efficiency and cost-effectiveness.

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

This task requires us to design a new passenger aircraft that minimizes the total weekly operating cost for Scenario 1 (3,300 passengers per week, maximum 13 flights per week, fuel price $0.85/kg, medium time-related cost). Only the cruise phase (T_best) is considered. The aircraft must obey a strict set of technical, regulatory, and economic rules that deliberately replicate real-world airline constraints and historical aviation practices. By systematically testing all feasible configurations, we identify the single most cost-effective design and name it under the name "HK Five55", which represents our group.

#### Scenarios

300-seat scenario:
A 300-seat aircraft is the smallest design that satisfies the 13-flight-per-week limit, requiring 11 flights to carry all 3,300 passengers (3,300 ÷ 300 = 11 exactly). Because it reaches the 300-seat threshold, it must be configured with four engines, incurring a fuel burn of 80 kg/min and a fixed cost of $2,500 per flight. Its time-related cost C_T is $20/min (12 + 2×4). Although it has the lowest variable rate among the four candidates ($88/min), the high number of flights (11) means the fixed cost is applied 11 times and the variable cost is charged for 11 × T_best minutes. This results in the highest weekly total of approximately $607,200 (at T_best = 600 min).

350-seat scenario:
Moving up to 350 seats reduces the required flights to 10 (3,300 ÷ 350 ≈ 9.43 → 10). The aircraft remains four-engine (ΔF = 80 kg/min), but C_T rises to $22/min because of one additional 50-seat block. The variable rate therefore increases to $90/min. Despite the higher per-minute cost, the saving of one entire flight eliminates one application of the $2,500 fixed cost and reduces total cruise minutes by T_best, yielding a clear cost reduction to around $564,000 — a saving of about $43,000 per week compared to the 300-seat design.

400-seat scenario:
With 400 seats, only 9 flights are needed (3,300 ÷ 400 = 8.25 → 9). The engine count and fuel burn remain identical to the previous two designs (four engines, 80 kg/min), but C_T climbs to $24/min, pushing the variable rate to $92/min. The further reduction from 10 to 9 flights again removes another $2,500 fixed cost and another full T_best of variable cost. The net effect is a further drop in weekly operating cost to approximately $523,800, demonstrating that the benefit of fewer flights continues to outweigh the rising per-minute charges.

450-seat scenario (optimal):
The 450-seat configuration is the largest permitted design and requires only 8 flights per week (3,300 ÷ 450 = 7.33 → 8). It still uses four engines and therefore the same 80 kg/min fuel burn, but C_T reaches the maximum of $26/min, giving the highest variable rate of $94/min. Nevertheless, operating just 8 flights instead of 11 (300-seat case) eliminates three complete applications of the $2,500 fixed cost and three full cruise segments of variable cost. These savings dominate the higher per-minute rate, delivering the lowest weekly total of $471,200 — approximately $136,000 cheaper per week than the 300-seat option and $52,600 cheaper than the 400-seat option. This confirms that, under a strict flight-frequency cap, economies of scale strongly favour the largest feasible aircraft.

#### Calculation

The total weekly operating cost is calculated using the formula C = N_flights × (C_F × ΔF × T_best + C_T × T_best + C_c). For any given seat count, the number of flights required is obtained by rounding up the ratio of 3,300 passengers to the aircraft capacity (N_flights = ⌈3300/seats⌉). Aircraft with 300 or more seats are assigned four engines (otherwise two), giving a fuel burn rate ΔF of 80 kg/min or 40 kg/min respectively at the fixed cruise consumption of 20 kg/min per engine. The time-related cost C_T starts at a base of $12/min and increases by $2 for every additional 50 passengers above 100 seats, yielding C_T values from $20/min (300 seats) to $26/min (450 seats). Adding the fuel cost component (0.85 × ΔF) to C_T produces the variable cost per minute, which is multiplied by the cruise duration T_best and then added to the fixed cost per flight ($2,000 for twin-engine, $2,500 for four-engine designs). The resulting per-flight cost is finally multiplied by the number of weekly flights. When this process is repeated for the four feasible capacities (300, 350, 400, and 450 seats), the 450-seat configuration consistently delivers the lowest total weekly cost — in the example of a 600-minute cruise, $471,200 — because the savings from operating only eight flights instead of eleven more than offset the higher per-minute variable rate and fixed cost associated with the largest four-engine aircraft. The following table shows the final costs of all scenarios.
<img width="767" height="454" alt="Screenshot 2025-11-24 010317" src="https://github.com/user-attachments/assets/9fd02bb9-38f1-443a-853a-3404c5a1a71f" />

<img width="1600" height="1122" alt="image" src="https://github.com/user-attachments/assets/fad2863c-418d-42e1-b0f2-ef0974263489" />

#### Bonus - Explaining the Rules and Restrictions


Rule 1: Passenger Capacity

Requirement: 100-450 seats, steps of 50

Real-world Reason/ Evidence: Covers narrow-body (≈100–200) to large wide-body (≈350–450) classes (A320 to A350/B777)


Rule 2: C_T scaling

Requirement: Base $12/min; +$2/min for every additional 50 seats above 100

Real-world Reason/ Evidence: Larger/heavier aircraft have higher crew cost, maintenance, depreciation, insurance, and cabin crew requirements per minute flown. Industry data show non-fuel cost per block minute rises almost linearly with size.


Rule 3: Must use 4 engines if seats >=300

Requirement: Mandatory switch at 300 seats

Real-world Reason/Evidence: Reflects historical ETOPS conservatism. Until the late 2000s, many regulators and airlines required four engines for very long over-water routes (e.g., South Pacific, polar). Although modern twins (B777, A350) are fully capable, the rule simulates a conservative authority or an ultra-long route where four engines are still mandated.


Rule 4: Fixed cost C_c

Requirement: $2,000 (twin-engine) vs $2,500 (4-engine)

Real-world Reason/Evidence: Four-engine aircraft have higher engine maintenance reserves, higher landing fees (due to higher MTOW), and more complex systems. Real B747 vs B777 data show ≈20–30 % higher trip cost for quads.


Rule 5: Engine fuel burn

Requirement: 20 kg/min per engine in cruise

Real-world Reason/Evidence: Simplified but realistic future high-bypass turbofan cruise burn (≈1.2 t/h per engine). Keeps calculations manageable.


Rule 6: Maximum 13 flights/week

Requirement: Limit to no more than 13 flights per week

Real-world Reason/Evidence: Represents slot constraints (e.g., London–Singapore) or aircraft utilization limits on ultra-long-haul routes (13 flights/week ≈ 1.85 daily turns).


Rule 7: Only cruise time counted

Requirement: Use T_best only

Real-world Reason/Evidence: On long-haul flights, cruise is 80–90 % of block time and dominates cost differences between designs.


## 6. Additional Task 1
<a href="taska1.py"><strong>Task A1 Code</strong></a>
### Description of task
This task is required modify the code in order to add two check points in each cost intensive area, and let the route pass through these check points before reaching the destination. 

### What was modified in the code?
The code from Task 1 was used to keep the template of our map with the specific cost intensive areas and obstacles. First, to add the check points on each cost intensive area, defining the coordinates of the check points is required before initialize the A Star Planner.

After that, we can use the A Star Planner to find the optimal route from start to check point 1, from check point 1 to check point 2, from check point 2 to final destination. These separate routes will then be added up together into one route from start to the final destination. The cost (in minutes) of these three segments will also be summed up to find the "Total path time (Tbest) across all segments", this will be printed on the top of the animation and in the output. 

A feature of the program is that the check points could be changed in line 281 and 283 where the coordinates of the check points are defined. Sensible results showing that the further the check points, the longer(Tbest) it takes for the route. 

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

A* was developed in 1968 by Peter Hart, Nils Nilsson, and Bertram Raphael. It is an algorithm that is widely used to find the shortest cost path between two points.

- **Dijkstra**

The Dijkstra path planning algorithm is a classic algorithm that is used to find the shortest path between nodes in a graph. It is developed by Edsger Dijkstra in 1956, and  it is widely used in network routing, robotics, and mapping applications.

- **RRT (Rapidly-exploring Random Tree)**

RRT was launched in 1998 by Steven M. LaValle. It is a path planning method for solving complex motion problems. It is especially applied in fields like robotics and autonomous vehicles.

---
### Theories
---
- **A***

A* is a smart path planning algorithm. It balances speed and accuracy well. Its core is a cost formula: f(n) = g(n) + h(n). Here, g(n) is the exact cost from the start node to the current node, and h(n) is a guess of the cost from the current node to the goal node. It uses two lists to track nodes: one for nodes we still need to check, and another one for nodes that we’ve already looked at. This method will avoid repeated work and therefore improve efficiency. If the guess h(n) never overestimates the real cost, A* will always find the shortest path. It works best for simple environments, such as the basic path planning in our tasks.

- **Dijkstra**

Dijkstra’s is a straightforward algorithm. It finds the shortest path in areas. First, Dijkstra sets the start node’s cost to 0. All other nodes start with an infinite cost. Then it keeps picking the node with the lowest current cost. Also, it updates the cost of the nearby nodes. It constantly does this until it reaches the goal. Dijkstra doesn’t use any guesses. It just checks all nodes in order of increasing cost. This guarantees the shortest path, but it could be slow for large spaces, since it checks irrelevant nodes too. In summary, it is  good for small and weighted graphs.

- **RRT**

RRT is a probabilistic algorithm. It uses randomness to find out paths. It is designed for complex environments. Usually, algorithms that are based on grids struggle in those environments. However, RRT builds a "random tree" to explore the space. It randomly picks a point, then finds the closest node in the existing tree, and connects them if the path is without obstacles. Sometimes, it prioritizes points near the goal to speed up pathfinding. RRT doesn’t guarantee the shortest path, but it is great for irregular spaces. For example, planning a drone’s flight path may need RRT.

---
### Performance （under task 1 scenario)
---
**A***

A* algorithms balance the speed and optimality in the grid, it ensure to find the shortest path by using Euclidean distance heuristic. Also its exploration on the goal, which can reduce unnecessary node checks and increase the efficiency. It can deal with the cost zones in an accurate way, and use moderate memory. In this task, A* is the best algorithm as it perform well in both efficiency and path optimality.


![astar_animation](https://github.com/user-attachments/assets/b471356e-3a17-4ac2-aed1-4acca2423925)


**Dijkstra**

Dijkstra’s algorithm find the shortest path by explores all possible nodes up to the goal. Although this algorithm can deal with the cost zones in an accurate way and give an optimal result, it takes a long time to checks many nodes, so its efficiency is very low. Additionally, it uses lots of memory to store all visited nodes. In this case, Dijkstra’s algorithm is acceptable but no the perfect one.


![dijkstra_path](https://github.com/user-attachments/assets/dcc0b2c0-fa4f-4f38-82a4-fe2f77621843)


**RRT**

Rapidly-exploring Random Tree can find the feasible path in a short time, as it find the path by random sampling and tree expansion which can prevent spending lots of time to check all the node. However, it can only deal with the cost zones in a rough way. Therefore, the path given might not be the optimal one. Also, random sampling makes the path change each run.


![rrt_path](https://github.com/user-attachments/assets/6431e695-deb6-4fa5-b6c7-eba1d5cae11c)



---
### Strengths and Limitations
---
### A*

#### Strengths:
A* works well if you pick a solid heuristic. It outperforms Dijkstra in large spaces because it focuses exploration on nodes closer to the goal. Moreover, it also guarantees an optimal path if the heuristic is reasonable and consistent. A star prioritizes nodes near the goal, which is highly effective for goal-directed tasks in both weighted and unweighted graphs.

#### Limitations:
A* is heuristic-dependent, since its performance relies heavily on the heuristic. It also uses a lot of memory, and keeps track of every possible path and their costs in two lists. This would become problematic in extremely large graphs. In addition, it’s trickier to set up than RRT or Dijkstra’s, since you need a good guess and have to manage a priority list of spots to check.



### Djikstra

#### Strengths:
Dijkstra’s algorithm always finds the shortest path if the path costs are not negative. It  offers simplicity as it is easier to implement than A*, and ensures completeness by finding a path if it exists.


#### Limitations:
Dijkstra’s algorithm is slow in large spaces since it explores every single node without heuristic guidance, which leads to inefficiency in large or dense graphs. Besides, it has high memory usage due to storing all visited nodes. Therefore, it becomes problematic for very large graphs, and suffers from checking irrelevant nodes. 



### RRT

#### Strengths:
RRT (Rapidly Exploring Random Tree) excels in high-dimensional spaces. It outperforms grid-based algorithms in large environments. Instead of tracking all explored nodes, RRT stores only a tree of sampled nodes, thereby having little memory usage. Additionally, it is adaptable to systems based on movement rules. For example, it works well for robots or vehicles with movement constraints.

#### Limitations:
RRT does not guarantee an optimal path. The random spots usually make the route longer than needed. It only achieves probabilistic completeness, and it’ll most likely find a path if one exists, but not 100% for sure. Moreover, the path quality is variable and depends heavily on parameters like sampling density and iteration count.

---

### Algorithm Comparison Summary

| Algorithm          | Theory                                                                 | Strengths                                                                 | Limitations                                                                 | Performance                                                 |
|--------------------|-----------------------------------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------------------------------------|
| **A\***            | - Cost function:  f(n) = g(n) + h(n)<br>- Nodes expansion with the lowest f(n) value | - Finds the shortest path if the heuristic is admissible | - Heuristic-dependent<br>- High memory usage for large graphs | - High efficiency with heuristic guidance        |
| **Dijkstra**       | - Cost function: g(n)<br>- Nodes expansion with the lowest g(n) values<br>- Uniform-cost search to ensure optimality | - Ensures completeness<br>- Guarantees optimality | - Low efficiency<br>- Requires lots of memory for large graphs    | - Explores all nodes up to the goal  |
| **RRT**            | - Grows a tree by randomly sampling and connecting  | - Able to handles complex obstacles | - Path is irregular and longer<br>- Variable as different path each run<br>- Cost zones handled roughly | - Path quality improves with more iterations<br>- Random → Each run give a different path|

<!-- Group Reflections -->
## 9. Group Reflections
Winkelhock, Yau Yue Hong Winkelhock (25034703D)

This group project has been a great milestone for me to dive into coding and an overview to GitHub. I am in charge of managing the GitHub repository, including the Readme file, as well as additional task 3. While I have no experience in either Python coding or HTML site coding, by discussion with groupmates, especially those who have learnt before, I am able to learn from their experience or even failures. Organising files and the readme contents are not easy, since there are coding skills required. I have faced barriers such as how to link each subheadings to the table of contents, as some subheadings works but the rest of them do not. Although I had tried for different attempts and approches, I am not able to solve the issue until I used AI for assitance. This again proves from lectures that GenAI could be useful in certain extents. And with their assistance, and of course our group's hard work, this readme, GitHub repository and all codes are smoothly run. I am certain that knowledge from this course is crucial through my university life and career usage in the aviation industry.

Rodgers, Rodgers Mawalla Maighacho (25094994D)

The group project enabled me to gain numerous collaboration and leadership skills. By overseeing the project, I learnt the positive effect of adhering to mini-deadlines, i.e finishing presentation slides within a weekend and ensuring everyone stays up to date with their tasks. I gained some coding knowledge from the coding leader, through whom I learnt to update our code in GitHub and run it to ensure it satisfies the assessment criteria. Additionally, through the lectures, I was able to acquire skills to be efficient in using AI to modify and correct various code segments, making the work cleaner and easier to interpret, especially for me as a coding beginner. In managing task 2, which involved finding an optimum cost area based on set restraints (5% reduction cost along the jet stream and specific jet stream dimensions), I was able to understand how the AStar planner 

August, Wang Tiancheng (25095793D)

Before this project, I had absolutely no programming background and even felt overwhelmed when I first saw the code files. However, I'm really interested in aircrafts and their path planning, so I made my decision to trymy best. At first, I struggled to even run the test cases, but I watched beginner tutorials in my free time and practiced step by step—gradually, I could not only verify the algorithm’s outputs but also spot small formatting errors in the code comments. In the process of completing additional tasks, I even learn more about Python. Our group is really collaborative, everyone focus on their tasks and help each other. This experience taught me that group collaboration turns daunting challenges into manageable steps. I didn’t just learn the basics of coding and documentation, but also how to ask for help and contribute to a team even when I’m new to a skill. It’s been a valuable lesson that I’ll carry into future group work.

Manny, So Yee Man (25079801D)

Talia, Cheung Yung Ting Talia (25129573D)

This project has gave me a glance at how flight planning works in the aviation industry, I find it most interesting is that flight planning requires check points in order to make flights safer and easier to plan. I've seen how artifical intelligent can help us human who's working for flight planning and aircraft designing through using code to summarise and calcuate datas all in one code. However, as my teammates and I have encountered countless of errors even with the AI generating the codes, we've learn the importance of verifying the codes with the data output by seeing if the numbers make sense when we input different datas. Using AI could also help me understand more about how coding works, such as learning about functions.

Sharon, Chan Chin Ying (25084065D)

This project provided me an invaluable experience in coding and flight planning. This was the first time ever in my life to  try not only modifying, but also designing new codes. and I witnessed the importance of the role played by artificial integlligence played in this project. As a frist-timer in coding, my teammates and I encountered a plethora of obstacles when designing the codes for the task, errors after errors. Had there not been the aid of AI, we wouldn't have been able to complete our tasks. With the aid of AI, not only did I learn to debug the codes, but also translate real-world contrains into logical codes. I was mainly responsible for task 3 in this project. One of the biggest difficulties was correctly implementing the C_T scaling rule with integer division. I initially used regular division and got wrong values. With the help of AI, I learnt to use math.ceil() for the number of flights, rounding up the values and ensuring the engine switch happened exactly at 300 seats. There are a lot more I learnt from AI in this project, this experience has given me real confidence in programming and has equipped me with practical skills that I will definitely carry into my future studies and career.

Sylvia, Lau Tsz Wing (25068927D)

In this group project, I learned how to use AI effectively to help me in completing tasks. For example, when writing the code, I initially gave a simple instruction to AI, ​​but I found that the results is always wrong, as lots of errors in these codes. After trying few time, I change to asked AI about the meaning of the words in the code. In addition to my understanding, I adjusted the code to achieve the result I wanted. AI also help me to improve my works, gave me ideas which saving my times and allow me to do more things. Moreover, I improved my collaboration and time management skills. Although this group project was not easy, cooperation and mutual assistance among every member made it easier to be complete. Meeting schedules with teammates, meeting deadlines, and breaking up the work into small goals taught me how to prioritize tasks and not rush things at the last minute.

<!-- Presentation Files -->
## 10. Presentation Files

