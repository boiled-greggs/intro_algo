import sys
import heapdict
from collections import defaultdict



def edit_distance(E, x, y):
    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if i == 0:
                E[i][j] = j
            elif j == 0:
                E[i][j] = i
            elif x[i-1] == y[j-1]:
                E[i][j] = E[i-1][j-1]
            else:
                E[i][j] = 1+min(E[i][j-1], E[i-1][j], E[i-1][j-1])
    return E

def alignment(E, x, y):
    str1 = ""
    str2 = ""
    i = len(x)
    j = len(y)
    while (i >= 0 and j >= 0):
        left = E[i][j-1]
        diag = E[i-1][j-1]
        up = E[i-1][j]

        if (min(left,diag,up) == diag):
            str1 += x[i-1]
            str2 += y[j-1]
            i -= 1
            j -= 1
        elif (min(left,diag,up) == left):
            str1 += '-'
            str2 += y[j-1]
            j -= 1
        else:
            str1 += x[i-1]
            str2 += '-'
            i -= 1
    print()

    for i in range(len(str1)-2,-1,-1):
        print(str1[i], end='')
    print()
    for i in range(len(str1)-2,-1,-1):
        print(str2[i], end='')

    print()
    print()
    return






if __name__ == "__main__":
    X = sys.argv[1]
    Y = sys.argv[2]

    #X = 'CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG'
    #Y = 'CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA'

    print(X)
    print(Y)
   
    E = [[0 for x in range(len(Y)+1)] for x in range(len(X)+1)]

    E = edit_distance(E, X, Y)
    print(E[len(X)][len(Y)])

    #for i in range(len(E)):
     #   print(E[i])

    alignment(E,X,Y)

