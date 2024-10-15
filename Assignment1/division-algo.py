# Payal Chavan
# CS5800 Algorithms Summer 2024 (Seattle)
# Homework 1
# Date: 05/15/2024



# Divide integer x by y != 0 to find Quotient and Remainder recursively

def divide(x, y):
    if x == 0:
        return 0, 0 # Quotient, Remainder

    q, r = divide(x // 2, y)
    q = q * 2
    r = r * 2
    # If x is odd, add 1 to the remainder
    if x % 2 != 0:
        r += 1
    # If remainder >= y, subtract y from remainder and add 1 to quotient
    if r >= y:
        r -= y
        q += 1

    return q, r


# Compare divide function's result  against the // operator (integer division).
def test_divide():
    test_cases = [(1234, 3), (76543, 41), (98436785, 571), (12457801, 67), (5067340011, 79)]
    for x, y in test_cases:
        q, r = divide(x, y)
        print(f"Dividing {x} by {y} using divide function: Quotient = {q}, Remainder = {r}")
        print(f"Dividing {x} by {y} using // operator: Quotient = {x // y}, Remainder = {x % y}")
        print()



# Time the divide function for different test cases
import time
import matplotlib.pyplot as plt
import random

def time_divide():
    x = 2
    scale = 100000
    times = []
    for i in range(1, 31):
        x = 2**i + random.randrange(0, 2**i)
        y = random.randrange(1, x)
        # y = 3
        print(f"Dividing {x} by {y}")
        start = time.perf_counter()
        for _ in range(10):
            divide(x, y)
        end = time.perf_counter()
        times.append((end - start) * scale)
    return times


if __name__ == '__main__':
    test_divide()

    times = time_divide()

    plt.figure(figsize=(12, 6))
    plt.plot(times)
    plt.xticks(range(1, 31))
    plt.xlabel("Number of Test Cases")
    plt.ylabel("Time (s)")
    plt.title("Time to Divide x by y")
    plt.savefig("division_algo_time_test")
    plt.show()
