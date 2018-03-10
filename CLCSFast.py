import sys
import numpy as np

arr = np.zeros((12, 7), dtype=int)


#
#
# To-Do not covered elsewhere: store lengths of paths/best path as we find it.
#
#

def find_shortest_path(A, B, p, lower, upper): #p
    m = len(A)/2
    n = len(B)
    if upper - lower <= 1:
        return
    mid = (lower + upper)/2
    p[mid] = single_shortest_path(A, B, mid, p[lower], p[upper], lower, upper)
    p[m+mid] = [[0,n] for i in range(0, m+1)]

    #
    # TODO: UNCOMMENT BELOW ONCE PATHS ARE APPROPRIATELY STORED IN SINGLE_SHORTEST_PATH
    #

    # find_shortest_path(A, B, p, lower, mid)
    # find_shortest_path(A, B, p, mid, upper)


#NOTE: Low row is low index, so UPPER BOUND
def single_shortest_path(A, B, mid, top_path, bottom_path, top_row, bottom_row):
    m = len(A)/2
    n = len(B)
    global arr

    print "BEFORE CLEAR: ", arr

    #
    #TODO: FIGURE OUT WHICH CLEARING IS NECESSARY (or if both are given odd/even case...)
    #
    #
    global arr
    #arr = np.zeros((12, 7), dtype=int)
    for i in range(0, n+1):
        arr[mid][i] = 0   #initialize early row of array. 
        arr[mid+1][i] = 0   #initialize early row of array. PROBABLY NOT NECESSARY BUT POTENTIALLY USEFUL until figuring out off-by-one-errors.

    print "AFTER CLEAR: ", arr
    print bottom_path, top_path
    #print "MID: ", mid
    for i in range(mid+1, m+mid+1):

        #print bottom_path[i][0]+1, top_path[i][1]

        for j in range(bottom_path[i][0] , top_path[i][1]+1): #+1 since col 0 is not used

            if i == 5:
                print "I = 5, j = ", j
            if A[i - 1] == B[j - 1] and (bottom_path[i-1][0] <= j - 1 <= top_path[i-1][1]):    # and in bounds ):
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                #TODO: ADD BOUND CHECKING BASED ON LOWER AND UPPER PATHS
                if (bottom_path[i-1][0] <= j <= top_path[i-1][1]):
                    if (bottom_path[i][0] <= j - 1): #not sure if we actually need to check this
                        arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
                else: #lol need to check this not sure if its right.
                    arr[i][j] = arr[i][j-1]
    print "AFTER GUIDED DP: ", arr

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
    return path

def LCS(A, B):
    m = len(A)
    n = len(B)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            #print A[i-1], "  ", B[i-1], " LCS"
            if A[i - 1] == B[j - 1]:
                arr[i][j] = arr[i - 1][j - 1] + 1
            else:
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    #print arr
    return arr[m][n]


def main():
    if len(sys.argv) != 1:
        sys.exit('Usage: `python LCS.py < input`')

    for l in sys.stdin:
        
        #A, B = "ACTCA", "TCGACG"
        A, B = l.split()
    
        m = len(A)
        n = len(B)
        p = [[] for i in range(0, 2*m)]
        #Update array for initialization, don't need to return anything from LCS
        LCS(A, B)
        p[0] = backtrace_full_LCS(A, B) + [[0,n] for i in range(0, m+1)]
        p[m] = [[0,n] for i in range(0, m)] + p[0]
        A = A + A
        print p[0]
        print p[m]
        # return
        find_shortest_path(A, B, p, 0, m)

        #
        #TODO: Take out break, print length of shortest path once we test.
        #

        break
    return


if __name__ == '__main__':
    main()