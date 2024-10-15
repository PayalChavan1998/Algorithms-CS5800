# Payal Chavan
# Summer 2024 
# Algorithms CS 5800
# Synthesis3 - Linear Programming
# Date: 08/09/2024


from scipy.optimize import linprog

# Coefficients of the objective function (maximize x1 + x2)
c = [-1, -1]  # Note: linprog performs minimization, so we use negative coefficients

# Coefficients of the inequality constraints
A = [
    [4, 2],  # Plumbing Inspector Constraint
    [2, 6],  # Electrical Inspector Constraint
    [4, 6]   # Building Inspector Constraint
]

# Right-hand side of the inequality constraints
b = [28, 30, 36]

# Bounds for the decision variables (x1 >= 0, x2 >= 0)
x_bounds = [(0, None), (0, None)]

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')

# Print the results
if result.success:
    print(f"Optimal number of gas stations to inspect: {-result.fun}")
    print(f"x1 - Optimal number of gas stations to inspect: {result.x[0]}")
    print(f"x2 - Optimal number of restaurants to inspect:  {result.x[1]}")

    # Plotting the feasible region
    import numpy as np
    import matplotlib.pyplot as plt

    x = np.linspace(0, 10, 400)
    y1 = (28 - 4 * x) / 2
    y2 = (30 - 2 * x) / 6
    y3 = (36 - 4 * x) / 6

    plt.figure(figsize=(10, 6))
    plt.plot(x, y1, label=r'$4x_1 + 2x_2 \leq 28$')
    plt.plot(x, y2, label=r'$2x_1 + 6x_2 \leq 30$')
    plt.plot(x, y3, label=r'$4x_1 + 6x_2 \leq 36$')
    plt.xlim((0, 10))
    plt.ylim((0, 10))
    plt.fill_between(x, np.minimum(np.minimum(y1, y2), y3), 0, where=(y1 >= 0) & (y2 >= 0) & (y3 >= 0), color='gray', alpha=0.5)

    # Plot the optimal solution
    plt.plot(result.x[0], result.x[1], 'ro', label='Optimal Solution')
    plt.xlabel(r'$x_1$ (Gas Stations)')
    plt.ylabel(r'$x_2$ (Restaurants)')
    plt.legend()
    plt.title('Feasible Region and Optimal Solution')
    plt.grid(True)
    plt.show()
else:
    print("No solution found.")








'''
Output:
Optimal number of gas stations to inspect: 8.0
x1 - Optimal number of gas stations to inspect: 6.0
x2 - Optimal number of restaurants to inspect:  2.0
'''