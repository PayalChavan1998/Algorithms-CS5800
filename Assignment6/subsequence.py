# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Contiguous Subsequence
# Computes the maximum sum in a contiguous subsequence
# Date: 06/28/2024



'''
A contiguous subsequence of a list S is a subsequence made up of consecutive elements of S.
For instance, if S is 5, 15, -30, 10, -5, 40, 10,
then 15, -30, 10 is a contiguous subsequence but 5, 15, 40 is not.

Give a linear-time algorithm for the following task:
Input: A list of numbers, a1, a2, · · · , an.
Output: The contiguous subsequence of maximum sum.
For the preceding example, the answer would be 10, -5, 40, 10, with a sum of 55.
(Hint: For each j ∈ 1, 2, · · · , n, consider contiguous subsequences ending exactly at position j.)
'''

# Import necessary functions
from random import randrange
from time import process_time


# Function to find the maximum contiguous subsequence in list A
def max_subsequence(A):
    max_sum = 0
    current_sum = 0
    start, end = 0, 0
    temp_start = 0

    for j in range(len(A)):
        current_sum += A[j]
        if current_sum < 0:
            current_sum = 0
            temp_start = j + 1

        if max_sum < current_sum:
            max_sum = current_sum
            start = temp_start
            end = j

    return max_sum, A[start : end+1]


# Function to find maximum sum and maximum subsequence for series of various lengths of elements
def test_max_subsequence():
    def output(sequence):
        max_sum, max_sub = max_subsequence(sequence)
        print(f"Sequence: {sequence} \nMax_Sum: {max_sum} for Max Subsequence: {max_sub}")
        print('- ' * 40)

    output([5, 15, -30, 10, -5, 40, 10])                            # len = 7 Dasgupta book example
    output([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11])         # len = 14
    output([3, -5, 1, 2, -1, 4, -3, 1, -2, 7, -6])                  # len = 11
    output([10, 15, -4, 5, -11, -3, 31, -25, 1, -23, 8, 31, -50])   # len = 13


# Function to find the run times of maximum contiguous subsequence
def test_time_max_subsequence():
    scale = 1000

    def run(length):
        times_list = []
        for _ in range(10):
            l = [randrange(-length, length) for _ in range(length)]
            start_time = process_time()
            max_subsequence(l)
            end_time = process_time()
            times_list.append((end_time - start_time)*scale)
        return times_list

    # Running time for 1000 elements
    times_1000 = run(1000)

    # Running time for 10000 elements
    times_10000 = run(10000)

    # Running time for 100000 elements
    times_100000 = run(100000)

    plot_graph(times_1000, times_10000, times_100000)


# Function to plot a graph to show run times for randomly generated 3 sequences
def plot_graph(t1, t2, t3):
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(12, 6))

    X = list(range(len(t1)))
    plt.plot(X, t1, label='1000 elements')
    plt.plot(X, t2, label='10000 elements')
    plt.plot(X, t3, label='100000 elements')

    plt.xlabel('Number of iterations')
    plt.xticks(range(len(t1)))
    plt.ylabel('Processing times in ms')
    plt.title('Processing time for list of 1000, 10000, 100000 elements')
    plt.legend()
    # plt.savefig()
    plt.show()


# Driver program to test max_subsequence and running time of max_subsequence
if __name__ == '__main__':
    test_max_subsequence()
    test_time_max_subsequence()
