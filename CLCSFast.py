import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)

# min_for_row = {}
# max_for_row = {}


def find_shortest_path(A, B, p, lower, upper): #p is a global variable for now
    if upper - lower <= 1:
        return
    mid = float(lower + upper)/2
    p[mid] = single_shortest_path(A, B, mid, p[lower], p[mid])
    find_shortest_path(A, B, lower, mid)
    find_shortest_path(A, B, mid, upper)


def single_shortest_path(A, B, mid, low_path, mid_path):
    return




def backtrace_full_LCS(A, B): 
    m = len(A)
    n = len(B)
    while m > 0 and n > 0:
        if A[m-1] == B[n-1]:
            #BACTRACE BY MOVING DIAGONAL. We have max for new row, and min for old row
            #min_for_row[m] = n --- STORE MAX index of ROW ARRAY to check (path bound)
            m = m - 1
            n = n - 1
        elif arr[m-1][n] < arr[m][n-1]:
            #BACKTRACE BY MOVING LEFT ON GRAPH. Update min for current row.
            n -= 1
        else:
            #BACKTRACE BY MOVING UP ON GRAPH. Update max for new row. 
            m -= 1






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
        p = [[] for i in range(0, 2m)]
        LCS(A, B)
        p[0] = backtrace_full_LCS(A, B)
        A = A + A
        find_shortest_path(A, B, p, 0, m)
    return


if __name__ == '__main__':
    main()