130. Surrounded Regions

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

1. go around the edge, look for Os, mark them S. 
add each S to a queue, use the queue to covert anything touching to S
convert all S to O
done

this is a BFS type approach. 

class Solution(object):
	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		if not board: return
		n, m = len(board), len(board[0])
		queue = []
		for i in range(m):
			self.helper(0, i, board, queue) 
			self.helper(n-1, i, board, queue) 
		for i in range(n):
			self.helper(i, 0, board, queue) 
			self.helper(i, m-1, board, queue) 
		print board
		while queue:
			x,y = queue.pop()
			if x >= 0 and x < n and y>=0 and y<m and board[x][y] =='O': 
				board[x][y] = 'S'
				queue.append((x,y+1))
				queue.append((x,y-1))
				queue.append((x+1,y))
				queue.append((x-1,y))
		for i in range(n):
			for j in range(m):
				if board[i][j]=='O':
					board[i][j]=='X'
		for i in range(n):
			for j in range(m):
				if board[i][j]=='S':
					board[i][j]=='O'
	def helper(self, x,y, board, queue):
		if board[x][y]=='O':
			board[x][y]='S'
			queue.append((x,y))


s = Solution()
s.solve(["XXXX","XOOX","XXOX","XOXX"])