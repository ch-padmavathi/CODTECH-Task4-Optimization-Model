from pulp import *

problem = LpProblem(
    "Profit_Maximization",
    LpMaximize
)

A = LpVariable("Product_A", lowBound=0)
B = LpVariable("Product_B", lowBound=0)

problem += 20 * A + 30 * B

problem += 2 * A + B <= 100
problem += A + 3 * B <= 90

problem.solve()

print("Optimization Results")
print("---------------------")

print("Product A =", A.varValue)
print("Product B =", B.varValue)

print("Maximum Profit = ₹", value(problem.objective))