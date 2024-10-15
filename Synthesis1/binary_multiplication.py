# CS 5800 Algorithms
# Summer 2024
# Payal Chavan
# Synthesis Assignment -1 
# Date: 06/07/2024


# Question: Compute binary multiplications for below given 5 test cases using Divide and Conquer Approach:
# Test case 1:(1100, 1010)) 
# Test case 2: (101, 101)
# Test case 3: (111, 111)
# Test case 4: (100, 100)
# Test case 5: (1111, 1111)


'''
code for binary multiplication with divide and conquer approach
The time complexity of the Karatsuba algorithm is O(n^log2(3)), where n is the number of digits in the larger of the two input numbers.
This is faster than the traditional multiplication algorithm, which has a time complexity of O(n^2).
The Karatsuba algorithm achieves this by reducing the number of basic multiplications required.
The algorithm is based on the observation that the product of two numbers is the sum of the products of their high and low bits, along with the product of their sum.
'''

def binary_multiplication(x, y):
    if len(str(x)) == 1 and len(str(y)) == 1:
        return x * y
    
    if len(str(x)) % 2 != 0:
        x = '0' + str(x)
    
    if len(str(y)) % 2 != 0:
        y = '0' + str(y)

    n = max(len(str(x)), len(str(y)))
    nby2 = n // 2

    a = int(x) // 10 ** nby2
    b = int(x) % 10 ** nby2
    c = int(y) // 10 ** nby2
    d = int(y) % 10 ** nby2

    ac = binary_multiplication(a, c)
    bd = binary_multiplication(b, d)
    ad_plus_bc = binary_multiplication(a + b, c + d) - ac - bd

    return ac * (2 ** n) + ad_plus_bc * (2 ** nby2) + bd

if __name__ == '__main__':
    print(binary_multiplication(1100, 1010)) # 120
    print(binary_multiplication(101, 101)) # 25
    print(binary_multiplication(111, 111)) # 49
    print(binary_multiplication(100, 100)) # 16
    print(binary_multiplication(1111, 1111)) # 225

'''
OUTPUT --

⚡ /usr/bin/python3 "/Users/payalchavan/Documents/Algorithms/Synthesis1_Assignment/Binary_Multiplication (1).py"
120
25
49
16
225
'''

