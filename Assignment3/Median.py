# Payal Chavan
# Summer 2024
# CS 5800 Algorithms (Seattle)
# Date: 05/30/2024

import random
import copy
import time

def swap( a, i, j ):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp
    return

# Given a list of numbers a
# Given an index containing the value on which to split the array
# Modifies the array in place so that it contains, in order
#   p values < a[index]
#   q values == a[index]
#   r values > a[index]
# The function returns (p, q, r)
def split( a, index ):

    # special case arrays of length 0 and 1 (shouldn't occur, but...)
    if len(a) == 0:
        return (0, 0, 0)
    
    if len(a) == 1:
        return (0, 1, 0)
    
    p = 0
    q = 1
    r = 0

    # swap a[index] with a[0]
    swap( a, index, 0)

    value = a[0]
    left = 1 # pointer to unchecked values <= v
    right = len(a)-1 # pointer to uncheck values > v

    # special case for an array of length 2
    if len(a) == 2:
        if a[left] < value:
            swap( a, 0, left )
            return (1, 1, 0)
        elif a[left] == value:
            return (0, 2, 0)
        else:
            return (0, 1, 1)

    # O(n) time
    while left < right:

        # move the left pointer right until we find a value > v or it meets right
        while left <= right:
            if a[left] <= value:
                left += 1 # move to the next location
                p += 1    # increase the number of items < v
            else: # a[left] > value
                break

        # move the right pointer left until we find a value < v or it meets left
        while left < right:
            if a[right] > value:
                right -= 1 # move pointer left
                r += 1     # increase the number of items > v
            else: # the value is <= v
                break;

        if left < right: # do a swap
            swap( a, left, right )


    # value in position 0
    # p values from index 1 to index p <= v
    # q values from index p+1 to end > v

    swap( a, 0, p ) # put the value v in between left right groups

    # get any other values in the left group that are = v
    left = 0
    # O(n) time, at most searches n-1 items
    while left < p:
        if a[left] == value:
            swap( a, left, p-1 )
            p -= 1 # subtract from group < v
            q += 1 # add to group == v
            left -= 1 # keep left where it is incase the value swapped in is = v
        left += 1

    # return the number of things in the three groups <, =, >
    return (p, q, r)

'''
RankSelect (A:valuelist, k:integer)
 R1: Calculate a pseudo-median m of the list A.
 R2: Determine the set A< of elements smaller than m.
 Determine the set A> of elements larger than m.
 Calculate the rank r of m in A.
 R3: If k<r then return RankSelect(A<, k)
 If k>r then return RankSelect(A>, k r)
 Else return m
'''
def rank_select( A, k ):
    # calculate the pseudo-median m of the list A
    m = middle_element( A )

    # determine the set A< of elements smaller than m
    A_less = [ x for x in A if x < m ]

    # determine the set A> of elements larger than m
    A_greater = [ x for x in A if x > m ]

    # calculate the rank r of m in A
    r = len(A_less)

    # if k < r then return RankSelect(A<, k)
    if k < r and len(A_less) > 0:
        return rank_select( A_less, k )

    # if k > r then return RankSelect(A>, k - r)
    if k > r and len(A_greater) > 0:
        return rank_select( A_greater, k - r )

    # else return m
    return m


'''
 Pseudo-Median (B:valuelist)
 P1: Break up the list B into quintets (groups of 5).
 P2: Calculate the median in each quintet (by brute-force). Call the result
 the representative of the quintet. There are n/5 representatives.
 P3: Return the median of the set of representatives:
 namely RankSelect(reps,n/10)
'''
def pseudo_median( B ):
    # break up the list B into quintets (groups of 5)
    quintets = [ B[i:i+5] for i in range(0, len(B), 5) ]

    # calculate the median in each quintet (by brute-force)
    representatives = [ middle_element( q ) for q in quintets ]

    # return the median of the set of representatives
    return rank_select( representatives, len(B)//10 )


# identify the 50th percentile value of the array a
def selection( a, k, use_pseudo_median=False):

    # base case where len(a) == 1, return value of the item in a
    if len(a) == 1:
        return a[0]

    # choose a value on which to split (choose a random index)
    if use_pseudo_median:
        pseudo_median_value = pseudo_median( a )
        index = a.index( pseudo_median_value )
    else:
        index = random.randint(0, len(a)-1 )

    # split to get p, q, r
    p, q, r = split( a, index )

    if k < p:
        # return a call selection with a[:p], k
        return selection( a[:p], k, use_pseudo_median)
    elif k < p + q:
        return a[p]
    else:
        # return a call to selection with a[p+r,:], k - (p + r)
        return selection( a[p+q:], k - (p + q), use_pseudo_median)


def middle_element( a: list):
    if len(a) == 0:
        return None

    return sorted(a)[len(a)//2]


def selection_compare(a: list, k: int):
    '''
    Python's built-in sort() function uses a sorting algorithm called "Timsort", which is a hybrid sorting algorithm derived from "merge sort" and "insertion sort". It is designed to perform well on many kinds of real-world data.
    The time complexity of Timsort is `O(n log n) in the worst case and average case`, and `O(n) in the best case (when the input is already sorted)`, making it one of the most efficient sorting algorithms in practical use.
    '''
    a.sort()
    return a[k]


def time_selection_pseudo_random_index():
    # scale time to microseconds
    scale = 1000000
    for n in range(1, 100, 10):
        a = [ random.randint(0, 1000) for i in range(n) ]   # list for selection with random index
        b = copy.deepcopy(a)    # list for selection with pseudo-median
        c = copy.deepcopy(a)    # list for selection with python built-in

        print(f"Array Size: {n}")
        k = random.randint(0, n-1)
        print(f"K: {k}")

        start_time = time.perf_counter()
        result = selection(a, k, False)
        end_time = time.perf_counter()
        selection_time = end_time - start_time
        print(f"Selection::Random-Index Value: {result}")
        print(f"Selection::Random-Index Time: {selection_time * scale:.2f} microseconds")

        start_time = time.perf_counter()
        result = selection(b, k, True)
        end_time = time.perf_counter()
        selection_pseudo_time = end_time - start_time
        print(f"Selection::Pseudo-Median Value: {result}")
        print(f"Selection::Pseudo-Median Time: {selection_pseudo_time * scale:.2f} microseconds")

        start_time = time.perf_counter()
        result = selection_compare(c, k)
        end_time = time.perf_counter()
        selection_py_builtin_time = end_time - start_time
        print(f"Selection::Python-Builtin Value: {result}")
        print(f"Selection::Python-Builtin Time: {selection_py_builtin_time * scale:.2f} microseconds")
        print("")


def test_selection():
    a = [44, 590, 722, 520, 708, 5, 32, 847, 3, 663, 847, 659, 425, 411, 635, 227, 743, 729, 438, 34, 698, 694, 471, 540, 500, 354, 561, 995, 243, 380, 959, 923, 903, 448, 993, 1, 478, 340, 477, 775, 193, 540, 395, 547, 600, 109, 972, 627, 547, 496, 260, 827, 319, 160, 625, 566, 562, 139, 536, 39, 870, 72, 372, 78, 928, 568, 792, 798, 24, 529, 298, 360, 109, 147, 521, 415, 49, 80, 663, 526, 333]
    b = copy.deepcopy(a)
    c = copy.deepcopy(a)
    k = len(a)//2 # middle element
    print(f"Selection::Random-Index Value: {selection(a, k, False)}")
    print(f"Selection::Pseudo-Median Value: {selection(b, k, True)}")
    print(f"Selection::Python-Builtin Value: {selection_compare(c, k)}")
    print("")


if __name__ == "__main__":
    test_selection()
    time_selection_pseudo_random_index()
