# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Assignment 8
# Coding Que2 - Generating Random 3-SAT Clauses
# Date: 07/29/2024



'''
Generating Random 3-SAT Clauses
Write a function that can generate random 3-SAT expressions given the number of variables N and the number of clauses C. Each expression should have only one instance of a given variable (e.g. not x1 or ^x1).
'''

import random
import string

def generate_3sat(N, C):
    """
    Generates a random 3-SAT problem with N variables and C clauses.
    Each clause contains exactly 3 literals, which can be either a variable or its negation.
    """
    variables = list(string.ascii_lowercase[:N])  # List of variables (a, b, c, ...)
    clauses = []
    for _ in range(C):
        clause = []
        variables_copy = variables.copy()  # Create a copy of the variables list
        for _ in range(3):
            variable = random.choice(variables_copy)  # Randomly select a variable from the copy
            variables_copy.remove(variable)  # Remove the selected variable from the copy
            if random.random() > 0.5:
                variable = f"~{variable}"   # Negate the variable with 50% probability
            clause.append(variable)    # Add the variable (or its negation) to the clause
        clauses.append(clause)  # Add the clause to the list of clauses
    return clauses


if __name__ == "__main__":
    # Generate and print a 3-SAT problem with 3 variables and 3 clauses
    print(generate_3sat(3, 3))
    # Generate and print a 3-SAT problem with 5 variables and 5 clauses
    print(generate_3sat(5, 5))
