# CS 5800 Algorithms
# Summer 2024
# Payal Chavan
# Synthesis Assignment -1 
# Date: 06/07/2024


'''
Merge Sort
Given an array of integers nums, sort the array in ascending order and return it.
You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]

Input: nums = [5,2,3,1]
Output: [1,2,3,5]

Input: nums = [9,8,7,6,5,4,3]
Output: [3,4,5,6,7,8,9]
'''

def mergeSort(nums):
    n = len(nums)
    if n == 1:
        return nums

    mid = n // 2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])
    return merge(left, right)


'''
It takes two sorted lists as input.
It creates a new list to hold the result.
It repeatedly takes the smallest element from the input lists and adds it to the result list.
It continues this process until both input lists are empty.
'''
def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    
    if left[0] <= right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


if __name__ == '__main__':
    nums = [5,1,1,2,0,0]
    print(f"Input: {nums} \t Output: {mergeSort(nums)}")

    nums = [5,2,3,1]
    print(f"Input: {nums} \t Output: {mergeSort(nums)}")

    nums = [9,8,7,6,5,4,3]
    print(f"Input: {nums} \t Output: {mergeSort(nums)}")


'''
OUTPUT -- 

payalchavan@Payals-MacBook-Air /Users/payalchavan/Documents/Algorithms/Synthesis1_Assignment                                                   
⚡ /usr/bin/python3 /Users/payalchavan/Documents/Algorithms/Synthesis1_Assignment/mergeSort.py
Input: [5, 1, 1, 2, 0, 0]        Output: [0, 0, 1, 1, 2, 5]
Input: [5, 2, 3, 1]      Output: [1, 2, 3, 5]
Input: [9, 8, 7, 6, 5, 4, 3]     Output: [3, 4, 5, 6, 7, 8, 9]
'''

