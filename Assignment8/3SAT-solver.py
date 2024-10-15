# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Assignment 8
# Coding Que1 - Write a solver for the 3-SAT problem
# Date: 07/29/2024


def read_clauses(filename):
    """
    Reads the 3-SAT clauses from a file and returns them as a list of lists.
    Each inner list represents a clause, where positive integers correspond to variables,
    and negative integers represent negated variables.
    """
    clauses = []
    with open(filename, 'r') as file:
        for line in file:
            clause = [int(x) for x in line.strip().split()]  # Convert each line to a list of integers
            clauses.append(clause)    # Add the clause to the list
    return clauses


def evaluate_clause(clause, assignment):
    """
    Evaluates a single 3-SAT clause given a variable assignment.
    Returns True if the clause evaluates to true, False otherwise.
    """
    for var in clause:
        if var > 0: 
            if assignment[abs(var) - 1]:  # Variable is true
                return True
        else:
            if not assignment[abs(var) - 1]:  # Negated variable is true
                return True
    return False     # Clause is false if none of the variables satisfy it


def exhaustive_search(clauses, num_vars):
    """
    Performs an exhaustive search over all possible variable assignments.
    Returns True if a satisfying assignment is found, False otherwise.
    """
    for i in range(2**num_vars):       # Iterate over all possible assignments
        assignment = [(i >> j) & 1 for j in range(num_vars)]  # Convert integer to binary list
        if all(evaluate_clause(clause, assignment) for clause in clauses):   # Check all clauses
            return True   # Satisfying assignment found
    return False   # No satisfying assignment found


def main():
    filename = '3sat_input.txt'  # input file
    num_vars = 4  # Adjust based on the number of variables in your input
    clauses = read_clauses(filename)
    if exhaustive_search(clauses, num_vars):     # Perform exhaustive search
        print("Satisfying assignment exists.")
    else:
        print("No satisfying assignment found.")


# Execute the main function
if __name__ == "__main__":
    main()
