# CS 5800 Algorithms
# Summer 2024
# Payal Chavan
# Synthesis Assignment -2
# Topic: Longest Increasing Subsequence (LIS) 
# Date: 07/10/2024



'''
Given an integer array nums, return the length and subsequence of the longest increasing subsequence
Input: [10, 9, 2, 5, 3, 7, 101, 18]
LIS subsequence: [2, 5, 7, 101]
Length of LIS:  4
'''


# Function to find Longest Increasing Subsequence (LIS)
def longest_increasing_subsequence(arr):
    n = len(arr)

    # LIS length ending at index. By default for every element LIS is 1
    lis_lengths = [1] * n

    # to track the parent index of subsequence ending at index, used for reconstructing sequence.
    prev_indices = [-1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and lis_lengths[i] < lis_lengths[j] + 1:
                lis_lengths[i] = lis_lengths[j] + 1
                prev_indices[i] = j

    # Find the maximum LIS length and its ending index
    max_length = max(lis_lengths)
    max_index = lis_lengths.index(max_length)

    # Reconstruct the LIS subsequence
    lis_subsequence = []
    while max_index != -1:
        lis_subsequence.append(arr[max_index])
        max_index = prev_indices[max_index]

    # Reverse to get the correct order
    lis_subsequence.reverse()
    return max_length, lis_subsequence

# Test Cases
def test_lis():
    tests_arr = [
        [10, 22, 9, 33, 21, 50, 41, 60, 80],
        [10, 9, 2, 5, 3, 7, 101, 18],
        [8, -6, 13, 1, 20, 2, 5, -9],
        [5, 5, 5, 5, 5, 5],
        [8, 7, 6, 5, 4],
        [4, 5, 6, 7, 8, 9]
    ]

    for arr in tests_arr:
        length, subsequence = longest_increasing_subsequence(arr)
        print("Array: \t\t", arr)
        print(f"LIS subsequence: {subsequence}")
        print(f"Length of LIS: \t{length}")
        print("-" * 50)


# Driver program to test the above function
if __name__ == '__main__':
    test_lis()



'''
OUTPUT

payalchavan@Payals-MacBook-Air /Users/payalchavan/Documents/Algorithms/Assignment4                                                           
⚡ /usr/bin/python3 /Users/payalchavan/Documents/Algorithms/Assignment4/LIS.py
Array:           [10, 22, 9, 33, 21, 50, 41, 60, 80]
LIS subsequence: [10, 22, 33, 50, 60, 80]
Length of LIS:  6
--------------------------------------------------
Array:           [10, 9, 2, 5, 3, 7, 101, 18]
LIS subsequence: [2, 5, 7, 101]
Length of LIS:  4
--------------------------------------------------
Array:           [8, -6, 13, 1, 20, 2, 5, -9]
LIS subsequence: [-6, 1, 2, 5]
Length of LIS:  4
--------------------------------------------------
Array:           [5, 5, 5, 5, 5, 5]
LIS subsequence: [5]
Length of LIS:  1
--------------------------------------------------
Array:           [8, 7, 6, 5, 4]
LIS subsequence: [8]
Length of LIS:  1
--------------------------------------------------
Array:           [4, 5, 6, 7, 8, 9]
LIS subsequence: [4, 5, 6, 7, 8, 9]
Length of LIS:  6
--------------------------------------------------
(base) 

'''