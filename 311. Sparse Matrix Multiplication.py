311. Sparse Matrix Multiplication

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

'''
Naive:
initialize the result matrix
for each element, compute the dot product of the corresponding row from A and column from B
this is a triple for loop, O(N^3)

Improvements:
Take advantage of the sparsity.
When we see a zero, no need to add anything ??? 
'''

def multiply(a,b):
	nrowa = len(a)
	ncola = len(a[0])
	nrowb = len(b)
	ncolb = len(b[0])
	# assertion, ncola==nrowb
	c = [[0] * ncolb for x in range(nrowa)]
	for i in range(nrowa):
		for j in range(ncolb):
			for k in range(ncola):
				c[i][j] += a[i][k] * b[k][j]
	return c


A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
multiply(A,B)

