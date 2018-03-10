import sys
import numpy as np

arr = np.zeros((2048, 2048), dtype=int)
max_lcs_length = 0
#
#
# To-Do not covered elsewhere: store lengths of paths/best path as we find it.
#
#

def find_shortest_path(A, B, p, lower, upper): #p
    m = len(A)/2
    n = len(B)
    #print "BEFORE"
    if upper - lower <= 1:
        #print "MIDDLE"
        #print max_lcs_length
        return
    #print "AFTER"
    mid = (lower + upper)/2
    p[mid] = single_shortest_path(A, B, mid, p[lower], p[upper], lower, upper)
    p[m+mid] = [[0,n] for i in range(0, m)] + p[mid]
    p[m+mid] = p[m+mid][0:len(A)+1]

    find_shortest_path(A, B, p, lower, mid)
    find_shortest_path(A, B, p, mid, upper)


#NOTE: Low row is low index, so UPPER BOUND
def single_shortest_path(A, B, mid, top_path, bottom_path, top_row, bottom_row):
    m = len(A)/2
    n = len(B)
    global arr

    #print "BEFORE CLEAR: ", arr

    #
    #TODO: FIGURE OUT WHICH CLEARING IS NECESSARY (or if both are given odd/even case...)
    #
    #
    global arr
    #arr = np.zeros((12, 7), dtype=int)
    for i in range(0, n+1):
        arr[mid-1][i] = 0 
        arr[mid][i] = 0   #initialize early row of array. 
        arr[mid+1][i] = 0   #initialize early row of array. PROBABLY NOT NECESSARY BUT POTENTIALLY USEFUL until figuring out off-by-one-errors.
        #arr[mid+2][i] = 0 

    #print "AFTER CLEAR: ", arr
    #print bottom_path, top_path
    #print "MID: ", mid
    for i in range(mid+1, m+mid+1):

        #print bottom_path[i][0]+1, top_path[i][1]

        for j in range(bottom_path[i][0], top_path[i][1]+1): #+1 since col 0 is not used
            if A[i - 1] == B[j - 1] and (bottom_path[i-1][0] <= j - 1 <= top_path[i-1][1]):    # and in bounds ):
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                #TODO: ADD BOUND CHECKING BASED ON LOWER AND UPPER PATHS
                if (bottom_path[i-1][0] <= j <= top_path[i-1][1]):
                    if (bottom_path[i][0] <= j - 1): #not sure if we actually need to check this
                        arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
                else: #lol need to check this not sure if its right.
                    arr[i][j] = arr[i][j-1]
   #print "AFTER GUIDED DP: \n", arr

    global max_lcs_length
    max_lcs_length = max(max_lcs_length, arr[i][j])

    n = len(B)
    m = len(A)
    path = [[0,n] for a in range(0, m+1)] #extra row
    while i > mid+1 and n > 0:
        if A[i-1] == B[n-1]:
            path[i-1][1] = n-1 #new row in upper bound case
            path[i][0] = n     #old row in lower bound case
            i = i - 1
            n = n - 1
        elif arr[i-1][n] < arr[i][n-1]:
            #BACKTRACE BY MOVING LEFT ON GRAPH. No updates necessary in upper bound case. 
                                                #min for row updated in lower bound case
            path[i][0] = n-1 #current row in lower bound case
            n -= 1
        else:
            #BACKTRACE BY MOVING UP ON GRAPH. Update max for new row in upper bound case. 
                                                #update min for old row in lower bound case
            path[i-1][1] = n #new row in upper bound case
            path[i][0] = n #old row in lower bound case
            i -= 1
    return path

    #
    #
    #TODO: BACKTRACE AND STORE PATH
    #
    #

    return #WE NEED TO DO THE BACKTRACE TO GET THE PATH

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
    global max_lcs_length
    max_lcs_length = lcs_length
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
        global arr 
        arr = np.zeros((2048, 2048), dtype=int)
        global max_lcs_length
        max_lcs_length = 0
        A, B = l.split()
       # A, B = "C", "CDCC"
        m = len(A)
        n = len(B)
        p = [[] for i in range(0, 2*m)]
        #Update array for initialization, don't need to return anything from LCS
        LCS(A, B)
        p[0] = backtrace_full_LCS(A, B) + [[0,n] for i in range(0, m+1)]
        p[m] = [[0,n] for i in range(0, m)] + p[0]
        A = A + A
        # return

        find_shortest_path(A, B, p, 0, m)

        #
        #TODO: Take out break, print length of shortest path once we test.
        print max_lcs_length        #
        #break
    return


if __name__ == '__main__':
    main()