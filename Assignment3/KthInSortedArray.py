# Payal Chavan
# Summer 2024
# CS 5800 Algorithms (Seattle)
# Date: 05/30/2024


# PART 1: Using Recursion Method

# given two sorted arrays, return the value of the kth element of their sorted union
def unionkth(array1: list, array2: list, k: int) -> int:
    # if array1 is empty, return the kth element of array 2
    if not array1 or len(array1) == 0:
        return array2[k]

    # if array2 is empty, return the kth element of array 1
    if not array2 or len(array2) == 0:
        return array1[k]

    # compute the two midpoint indexes of the arrays
    mid1 = len(array1) // 2
    mid2 = len(array2) // 2

    if mid1 + mid2 >= k:
        if array1[mid1] > array2[mid2]:
            return unionkth(array1[:mid1], array2, k)
        else:
            return unionkth(array1, array2[:mid2], k)
    else:
        if array1[mid1] > array2[mid2]:
            return unionkth(array1, array2[mid2 + 1:], k - mid2 - 1)
        else:
            return unionkth(array1[mid1 + 1:], array2, k - mid1 - 1)


# PART 2: Using Iterative Method

def unionkthIterative(arr1, arr2, k):
    def get(arr, i):
        if i < len(arr):
            return arr[i]
        return float('inf')

    # Start pointers for both arrays
    start1, start2 = 0, 0

    while True:
        if start1 == len(arr1):
            return arr2[start2 + k]
        if start2 == len(arr2):
            return arr1[start1 + k]
        # If k is 0, return the minimum of the first elements of both arrays
        if k == 0:
            return min(arr1[start1], arr2[start2])

        # Calculate the mid index for each array
        mid1 = start1 + (k + 1) // 2 - 1
        mid2 = start2 + (k + 1) // 2 - 1

        # Get the elements at mid indices (or infinity if the index is out of bounds)
        mid1_val = get(arr1, mid1)
        mid2_val = get(arr2, mid2)

        # Discard half of the elements from one of the arrays
        if mid1_val < mid2_val:
            # Move the start pointer of arr1
            k -= (mid1 - start1 + 1)
            start1 = mid1 + 1
        else:
            # Move the start pointer of arr2
            k -= (mid2 - start2 + 1)
            start2 = mid2 + 1


# PART 3: Using Python Built-in Method

def unionKthCompare(array1: list, array2: list, k):
    # join both arrays and sort them
    return sorted(array1 + array2)[k]


# Testing for finding kth element in union of two lists 

def test_unionKth():
    array1 = [1, 13, 25, 37, 49]
    array2 = [22, 24, 26, 88, 90]

    for k in range(len(array1) + len(array2) ):
        print(f"unionkth: {unionkth(array1, array2, k)} -- unionkthIterative: {unionkthIterative(array1, array2, k)} -- unionKthCompare: {unionKthCompare(array1, array2, k)}")


if __name__ == '__main__':
    test_unionKth()
