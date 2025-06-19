# OPTIMIZATION-MODEL

NAME: RASHMI KUMARI

INTERN ID:CT04DN978

DOMAIN: DATA SCIENCE

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

TASK DESCRIPTION 

Task 4: Production Optimization using Linear Programming

 Objective:

The objective of Task 4 is to apply linear programming concepts to solve a real-world production optimization problem. The company produces two products, A and B, and aims to determine how many units of each to produce in order to maximize profit while staying within constraints on labor and material availability.

 Business Problem:

The company earns profit by selling:

Product A: ₹30 per unit

Product B: ₹50 per unit


Resources available are limited:

Labor: 2 hours required for Product A and 4 hours for Product B (maximum available: 400 hours)

Material: 3 kg required for Product A and 2 kg for Product B (maximum available: 300 kg)


Goal: Maximize profit without exceeding the available labor and material.


ools & Technologies Used:

Python 3.x: Core programming language

PuLP: A Python library for linear programming

VS Code / Jupyter Notebook: To write and execute code


 Implementation Steps:

 Step 1: Import the PuLP Library

First, we import classes like LpProblem, LpMaximize, LpVariable, and value from the PuLP library to help define and solve our problem.

 Step 2: Define the Problem

We create a linear programming model and define it as a maximization problem because our objective is to maximize profit.

 Step 3: Create Decision Variables

Define two variables:

Units_of_A: Number of units of Product A

Units_of_B: Number of units of Product B Both are continuous and non-negative.


 Step 4: Define the Objective Function

The profit function is:

Profit = 30 * Units_of_A + 50 * Units_of_B

This is the function we want to maximize.

 Step 5: Add Constraints

Constraints are added to ensure we do not exceed available resources:

Labor: 2 * A + 4 * B ≤ 400

Material: 3 * A + 2 * B ≤ 300


 Step 6: Solve the Problem

We solve the model using PuLP's built-in .solve() method. The solver evaluates all combinations and returns the optimal values for the decision variables.

 Step 7: Output Results

Once solved, the model prints:

Number of units of Product A to produce

Number of units of Product B to produce

Maximum achievable profit


Sample Output:

--- Production Optimization - Friend Version ---
Total Status: Optimal
Produce Product A: 50.0 units
Produce Product B: 75.0 units
Max Profit (₹): 6000.0





---

 Conclusion:

This task clearly demonstrated how linear programming can be used to solve optimization problems. It is a great example of how data science techniques can be applied in business scenarios like production planning and resource management. Using the PuLP library in Python, we successfully formulated the problem, implemented constraints, and derived the most profitable solution. This experience builds a solid understanding of how data-driven decision-making works in practice.

---

