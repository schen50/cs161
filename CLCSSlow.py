import sys
import numpy as np

arr = np.zeros((4001, 4001), dtype=int)

def LCS(A,B):
	m = len(A)
	n = len(B)

	for i in range(1,m+1):
		for j in range(1,n+1):
			if A[i-1] == B[j-1]:
				arr[i][j] = arr[i-1][j-1]+1
			else:
				arr[i][j] = max(arr[i-1][j], arr[i][j-1])

	return arr[m][n]

def cut(str, index):
	return str[index:] + str[0:index]

def main():
	if len(sys.argv) != 1:
		sys.exit('Usage: `python LCS.py < input`')
	for l in sys.stdin:
		A,B = l.split()
		m = len(A)
		n = len(B)
		global arr
		arr = np.zeros((m+2, n+2), dtype=int)
		print max(LCS(cut(A, i), B) for i in range(0, len(A)))
	return

if __name__ == '__main__':
	main()