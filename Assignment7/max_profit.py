# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Assignment 7
# Coding Que2 - Max Profit
# Date: 07/20/2024



#Import necessary libraries
import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Coefficients of the objective function (maximize 1.6x1 + 1.4x2)
# Convert to minimization by using negative coefficients
c = [-1.6, -1.4]

# Coefficients of the inequality constraints
A = [
    [1, 2],       # x1 + 2x2 <= 240000
    [1.5, 1],     # 1.5x1 + x2 <= 180000
    [1, 0],       # x1 <= 110000
    [-1, 0],      # x1 >= 0 (converted to -x1 <= 0)
    [0, -1]       # x2 >= 0 (converted to -x2 <= 0)
]

# Right-hand side of the inequality constraints
b = [240000, 180000, 110000, 0, 0]

# Bounds for each variable
x1_bounds = (0, None)  # x1 >= 0
x2_bounds = (0, None)  # x2 >= 0

# Solve the linear program
result = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds], method='highs')

# Extract the optimal values of x1 and x2
x1, x2 = result.x

# Print the optimal values of x1, x2, and objective function
print("Optimal value of x1:", x1)
print("Optimal value of x2:", x2)
print("Maximum value of the objective function:", -result.fun)

# Plotting the feasible region
x = np.linspace(0, 120000, 400)
y1 = (240000 - x) / 2
y2 = 180000 - 1.5 * x
y3 = 110000 * np.ones_like(x)
y4 = np.ones_like(x)
y5 = np.ones_like(x)

# Customize the plot by adding labels
plt.figure(num='Feasible Region and Optimal Solution', figsize=(10, 8))
plt.plot(x, y1, label=r'$x_1 + 2x_2 \leq 240000$')
plt.plot(x, y2, label=r'$1.5x_1 + x_2 \leq 180000$')
plt.plot(x, y3, label=r'$x_1 \leq 110000$')
# plt.plot(x, y4, label=r'$x_2 \geq 0$')
# plt.plot(x, y5, label=r'$x_1 \geq 0$')

# Fill the feasible region
plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), where=(x <= 110000), color='gray', alpha=0.5)

plt.xlim((0, 120000))
plt.ylim((0, 120000))
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.axhline(0, color='black', lw=2)
plt.axvline(0, color='black', lw=2)
plt.scatter(x1, x2, color='red', zorder=5)
plt.text(x1, x2, f'({x1:.2f}, {x2:.2f})', fontsize=12, verticalalignment='bottom')
plt.legend()
plt.show()
