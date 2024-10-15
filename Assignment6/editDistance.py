# Bruce A. Maxwell
# Payal Chavan
# Summer 2024 (Seattle)
# CS 5800
# Edit Distance
# Computes the edit distance between two strings given on the command line
# Date: 06/28/2024

import sys

# Given two strings, computes the edit distance between them
# Returns the edit distance, the table of matches, and the table of parents
# back-tracking the parent table shows the matching
# Moving left skips a character of B (delete a B character)
# Moving up skips a character of A (insert an A character)
# Moving diagonally is either a match or a substitution
def editDistance( A, B ):

    # define insert distance (1)
    insert_dist = 1
    # define delete distance (1)
    delete_dist = 1
    # define substitution distance (1)
    sub_dist = 1

    # put a gap character "_" in front of both strings
    A = "_" + A
    B = "_" + B

    # create a table and a parent array
    table = [[0 for j in range(len(B))] for i in range(len(A))]
    parent = [[0 for j in range(len(B))] for i in range(len(A))]

    # fill in the top row using insert distance
    for j in range(1, len(B)):
        table[0][j] = table[0][j-1] + insert_dist
        parent[0][j] = 1

    # fill in the rest of the first column using delete distance
    for i in range(1, len(A)):
        table[i][0] = table[i-1][0] + delete_dist
        parent[i][0] = 2

    # fill in the rest of the table
            # test up (delete), diagonal left (match/sub), and left (insert)
            # assign table and parent to the min value found
    for i in range(1, len(A)):
        for j in range(1, len(B)):
            up = table[i-1][j] + delete_dist
            left = table[i][j-1] + insert_dist
            if A[i] == B[j]:
                sub = table[i-1][j-1]
            else:
                sub = table[i-1][j-1] + sub_dist
            if up < left and up < sub:
                table[i][j] = up
                parent[i][j] = 2
            elif left < sub:
                table[i][j] = left
                parent[i][j] = 1
            else:
                table[i][j] = sub
                parent[i][j] = 3

    # return the edit distance (lower right of the table), table, and parent array
    return table[len(A)-1][len(B)-1], table, parent

# Main function, given the command line arguments
def main(argv):

    # check if there are enough arguments
    if len(argv) < 3:
        print( "usage: python3 %s <word A> <word B>" % (argv[0]) )
        return

    # get the two strings
    A = argv[1]
    B = argv[2]

    print("Edit distance between '%s' and '%s'" % (A, B) )

    # compute the edit distance
    edist, table, parent = editDistance( A, B )

    # print out the edit distance and the table
    print("Distance: %d" % (edist) )
    print("Table:")

    s = "    _ "
    for c in B:
        s += " " + c + " "
    print(s)

    s = " _ "
    for j in range(len(B)+1):
        s += "%2d " % (table[0][j])
    print(s)

    for i in range(1, len(A)+1):
        s = " " + A[i-1] + " "
        for j in range(len(B)+1):
            s += "%2d " % (table[i][j])
        print(s)

    return

if __name__ == "__main__":
    main(sys.argv)
