# CS 5800 Algorithms
# Summer 2024
# Payal Chavan
# Synthesis Assignment -1 
# Date: 06/07/2024


'''
Write quick sort algorithm implementation
'''
def quickSort(nums: list, start, end):
    if start > end:
        return

    pivot = partition(nums, start, end)
    # this pivot is partition index,
    # it is fixed in the final Sorted list

    quickSort(nums, start, pivot - 1)
    quickSort(nums, pivot + 1, end)
    return nums


def partition(nums: list, start, end):
    # select last element as pivot
    pivot = end
    # pivot_index for swapping
    pivot_index = start - 1
    for j in range(start, end):
        # index value < pivot value then swap the pivot_index
        if nums[j] < nums[pivot]:
            pivot_index += 1
            nums[pivot_index], nums[j] = nums[j], nums[pivot_index]

    nums[pivot_index + 1], nums[pivot] = nums[pivot], nums[pivot_index + 1]
    return pivot_index + 1


if __name__ == '__main__':
    nums = [5,1,1,2,0,0,9]
    print(f"Input: {nums} \t Output: {quickSort(nums, 0, len(nums) - 1)}")

    nums = [5, 2, 7, 3, 1]
    print(f"Input: {nums} \t Output: {quickSort(nums, 0, len(nums) - 1)}")

    nums = [9,8,7,6,1,5,4,3]
    print(f"Input: {nums} \t Output: {quickSort(nums, 0, len(nums) - 1)}")


'''
OUTPUT --

⚡ /usr/bin/python3 /Users/payalchavan/Documents/Algorithms/Synthesis1_Assignment/QuickSort.py
Input: [5, 1, 1, 2, 0, 0, 9]     Output: [0, 0, 1, 1, 2, 5, 9]
Input: [5, 2, 7, 3, 1]   Output: [1, 2, 3, 5, 7]
Input: [9, 8, 7, 6, 1, 5, 4, 3]          Output: [1, 3, 4, 5, 6, 7, 8, 9]
'''
