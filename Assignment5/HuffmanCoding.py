# Bruce A. Maxwell
# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Huffman Coding implementation
# Date: 06/21/2024

from simple_heap import PQ

# compare the frequencies of two nodes, ascending order
def compareup( a, b ):
    return a.freq() < b.freq()

# Simple Node class for Huffman coding
class HNode:

    def __init__(self, id, freq, left, right ):
        self._left = left
        self._right = right
        self._freq = freq
        self._id = id
        self._code = ""

    def id(self):
        return self._id
        
    def left(self):
        return self._left

    def right(self):
        return self._right

    def freq(self):
        return self._freq

    def setCode(self, c):
        self._code = c
    
    def code(self):
        return self._code

# DFS on a binary tree, building codes
def exploreCodes(n, s):

    if n.left() != None:
        exploreCodes(n.left(), s + "0")

    if n.right() != None:
        exploreCodes(n.right(), s + "1")

    if n.left() == None and n.right() == None:
        n.setCode( s )
        print(n.id(), n.code())
        bits_required(n.freq(), n.code())


required_bits = 0
def bits_required(freq, code):
    global required_bits
    required_bits += freq * len(code)



"""
Encode the given letters using Huffman coding algorithm.

Args:
    letters (list): A list of letters to be encoded.
    freq (list): A list of frequencies corresponding to each letter.

Returns:
    list: A list of nodes representing the Huffman encoding tree.
"""
def huffman_encode(letters: list, freq: list ):
    nodes = []

    total_freq = len(freq)
    pq = PQ(total_freq, compareup)

    for i in range(total_freq):
        pq.add(HNode(letters[i], freq[i], None, None))

    for k in range(total_freq, total_freq * 2 - 1):
        i = pq.remove()
        j = pq.remove()
        n = HNode(k, i.freq() + j.freq(), i, j)

        nodes.append(n)
        pq.add(n)

    return nodes


def test_huffman_encode():
    letters = ["BLANK", "e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]
    freq = [ 18.3, 10.2, 7.7, 6.8, 5.9, 5.8, 5.5, 5.1, 4.9, 4.8, 3.5, 3.4, 2.6, 2.4, 2.1, 1.9, 1.8, 1.7, 1.6, 1.6, 1.3, 0.9, 0.6, 0.2, 0.2, 0.1, 0.1]
    nodes = huffman_encode(letters, freq)

    global required_bits

    # DFS on the last node
    exploreCodes( nodes[-1], "")
    print("Bits required: {:.2f}".format(required_bits))

    print("-"*25)

    letters = ['A', 'C', 'G', 'T']
    freq = [ 0.31, 0.2, 0.09, 0.4 ]
    nodes = huffman_encode(letters, freq)

    required_bits = 0
    # DFS on the last node
    exploreCodes( nodes[-1], "")
    print("Bits required: {:.2f}".format(required_bits))

if __name__ == "__main__":
    test_huffman_encode()


'''
Output: 

Below is the output of exercise 5.18 and 5.13 

'''