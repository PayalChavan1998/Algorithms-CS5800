# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Assignment 8
# Coding Que3 - Experiment
# Date: 07/29/2024



'''
Explore how the number of variables and the number of clauses interact by calculating the percentage of random expressions that have a solution for a given number of variables and a given number of clauses. 
At the very least, for 3 numbers of variables (e.g. N = 10, 16, 20), evaluate the percentage of expressions that have a solution for C=1 to C=10*N and show the result in a graph. 
For example, for each value of C, generate 100 random clauses and evaluate what percent have a solution.
If you want to get fancier, make a graph with N on the x-axis and C on the y-axis and have the color of the plot indicate the % of random clauses that have a solution.
'''

import random
import string
import matplotlib.pyplot as plt
import numpy as np

def generate_3sat(N, C):
    """
    Generates a random 3-SAT problem with N variables and C clauses.
    Each clause contains exactly 3 literals, which can be either a variable or its negation.
    """
    variables = list(string.ascii_lowercase[:N])  # List of variables (a, b, c, ...)
    clauses = []
    for _ in range(C):
        clause = []
        variables_copy = variables.copy()  # Randomly select a variable from the copy
        for _ in range(3):
            variable = random.choice(variables_copy)  # Use the copy of the variables list
            variables_copy.remove(variable)   # Remove the selected variable from the copy
            if random.random() > 0.5:
                variable = f"~{variable}"
            clause.append(variable)
        clauses.append(clause)
    return clauses


def check_solution(clauses, solution):
    """
    Checks if a given solution satisfies all the clauses.
    Returns True if the solution satisfies all clauses, False otherwise.
    """
    for clause in clauses:
        if not any([literal in solution for literal in clause]):   # Check if any literal in the clause is in the solution
            return False    # Clause is not satisfied
    return True   # All clauses are satisfied


def generate_random_solution(N):
    """
    Generates a random solution for N variables.
    Each variable can be either positive or negated.
    """
    variables = list(string.ascii_lowercase[:N])  # List of variables (a, b, c, ...)
    solution = []
    for variable in variables:
        if random.random() > 0.5:
            variable = f"~{variable}"
        solution.append(variable)   # Add the variable (or its negation) to the solution
    return solution


def calculate_percentage(N, C, num_experiments):
    """
    Calculates the percentage of random solutions that satisfy the 3-SAT problem.
    Runs num_experiments experiments for a given number of variables (N) and clauses (C).
    """
    num_solutions = 0
    for _ in range(num_experiments):
        clauses = generate_3sat(N, C)            # Generate random 3-SAT clauses
        solution = generate_random_solution(N)   # Generate a random solution
        if check_solution(clauses, solution):    # Check if the solution satisfies the clauses
            num_solutions += 1
    return num_solutions / num_experiments       # Calculate the percentage of satisfying solutions


if __name__ == "__main__":
    N_values = [4, 8, 12]       # Different numbers of variables to test
    C_values = list(range(1, max(N_values)*10+1, 5))   # Different numbers of clauses to test
    num_experiments = 100    # Number of experiments to run for each combination of N and C
    percentages = np.zeros((len(C_values), len(N_values)))   # Initialize a matrix to store the percentages
    for i, N in enumerate(N_values):
        for j, C in enumerate(C_values):
            percentages[j, i] = calculate_percentage(N, C, num_experiments)  # Calculate the percentage for each combination


    # Create a graph having N on the x-axis and C on the y-axis and the color of the plot indicates the % of random clauses that have a solution.
    plt.figure(figsize=(6, 8))
    plt.imshow(percentages, cmap="viridis", interpolation="nearest")    # Display the percentages as an image
    plt.xticks(np.arange(len(N_values)), N_values)
    plt.xlabel("Number of Variables")
    plt.yticks(np.arange(len(C_values)), C_values)
    plt.ylabel("Number of Clauses")
    plt.title("Percentage of Random Expressions with a Solution")
    plt.colorbar()
    plt.show()
