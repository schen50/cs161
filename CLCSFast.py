import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)


def find_shortest_path(A, B, p, lower, upper): #p
    if upper - lower <= 1:
        return
    mid = float(lower + upper)/2
    print p[lower]
    print p[upper]
    p[mid] = single_shortest_path(A, B, mid, p[lower], p[upper])
    find_shortest_path(A, B, lower, mid)
    find_shortest_path(A, B, mid, upper)

def single_shortest_path(A, B, mid, low_path, upper_path):
    return

#[(Min for lower bound INCLUSIVE, max for upper bound INCLUSIVE)]

def backtrace_full_LCS(A, B): #Maybe only use for path 0 case? Then write more elaborate method for boundary checking?
    m = len(A)
    n = len(B)
    lcs_length = 0
    path = [[0,n] for i in range(0, m+1)] #extra row
    while m > 0 and n > 0:
        if A[m-1] == B[n-1]:
            path[m-1][1] = n-1 #new row in upper bound case
            path[m][0] = n     #old row in lower bound case
            m = m - 1
            n = n - 1
            lcs_length += 1
        elif arr[m-1][n] < arr[m][n-1]:
            #BACKTRACE BY MOVING LEFT ON GRAPH. No updates necessary in upper bound case. 
                                                #min for row updated in lower bound case
            path[m][0] = n-1 #current row in lower bound case
            n -= 1
        else:
            #BACKTRACE BY MOVING UP ON GRAPH. Update max for new row in upper bound case. 
                                                #update min for old row in lower bound case
            path[m-1][1] = n #new row in upper bound case
            path[m][0] = n #old row in lower bound case
            m -= 1
    return path

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
        p = [[] for i in range(0, m+1)]
        #Update array for initialization, don't need to return anything from LCS
        LCS(A, B)
        p[0] = backtrace_full_LCS(A, B)
        p[m] = p[0]
        A = A + A
        find_shortest_path(A, B, p, 0, m)
    return


if __name__ == '__main__':
    main()