
"""
Business Problem:
A company makes Product A and B with limited resources.
- Product A generates ₹30 profit per unit
- Product B generates ₹50 profit per unit

Constraints:
- Product A requires 2 labor hours and 3 kg material
- Product B requires 4 labor hours and 2 kg material
- Total labor available: 400 hours
- Total material available: 300 kg

Objective:
Find the ideal number of A and B units to produce for max profit.
"""

# Step 1: Import PuLP library
from pulp import LpProblem, LpMaximize, LpVariable, value

# Step 2: Define the optimization problem (maximization)
prob = LpProblem("Profit_Max_Problem", LpMaximize)

# Step 3: Define decision variables (non-negative)
prod_a = LpVariable("Units_of_A", lowBound=0)
prod_b = LpVariable("Units_of_B", lowBound=0)

# Step 4: Objective function — maximize profit
prob += 30 * prod_a + 50 * prod_b, "Total_Profit"

# Step 5: Add resource constraints
prob += 2 * prod_a + 4 * prod_b <= 400, "Labor_Limit"
prob += 3 * prod_a + 2 * prod_b <= 300, "Material_Limit"

# Step 6: Solve the optimization problem
prob.solve()

# Step 7: Display results
print("\n--- Production Optimization - Friend Version ---")
print("Total Status:", prob.status, "-", prob.status)
print("Produce Product A:", prod_a.varValue, "units")
print("Produce Product B:", prod_b.varValue, "units")
print("Max Profit (₹):", value(prob.objective))