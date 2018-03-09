import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)



def find_shortest_path(A, B, p, lower, upper): #p is a global variable for now
    if upper - lower <= 1:
        return
    mid = float(lower + upper)/2
    p[mid] = single_shortest_path(A, B, mid, p[lower], p[mid])
    find_shortest_path(A, B, lower, mid)
    find_shortest_path(A, B, mid, upper)


def single_shortest_path(A, B, mid, low_path, mid_path):
    return 


def LCS(A, B):
    m = len(A)
    n = len(B)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

    return arr[m][n]


def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')

    for l in sys.stdin:
        A, B = l.split()
        m = len(A)
        p = [[] for i in range(0, m)]
        A = A + A
        paths[0] = single_shortest_path(A, B, p, [], [])
        find_shortest_path(A, B, p, 0, m)
    return


if __name__ == '__main__':
    main()