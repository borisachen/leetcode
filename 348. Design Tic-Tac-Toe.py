348. Design Tic-Tac-Toe

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?
-----------------------------------
Naively, we can do the moperation in O(n^2)
by checking every row, columns, and diagonal each move.

We can improve this by using storage.

Option 1 is a dictionary or dictionaries with all the winning arrays, then whenever we see a move,
we update X in the 2 or 3 positions. 
We check for a winner if any of the dictionaries has a 3 counter

Option 2: use +1 and -1 for the players.
We can track each of the n rows and n cols by starting with 0
then increasing or decreasing by +/-1 for each move.
If any counter ever gets to +n or -n, then we have a winner

-----------------------------------

class tictactoe(object):
	def __init__(self, n):
		self.rows = [0] * n
		self.cols = [0] * n
		self.d1 = 0
		self.d2 = 0
		self.n = n
	def move(self, player, r, c):
		if player != 1: 
			player = -1
		self.rows[r] += player
		self.cols[c] += player
		if abs(self.rows[r]) == self.n: return player
		if abs(self.cols[c]) == self.n: return player
		if r == c:
			self.d1 += player
			if abs(self.d1) == self.n: return player
		if r == self.n - c - 1:
			self.d2 += player
			if abs(self.d2) == self.n: return player
		return 0

toe = tictactoe(3)

toe.move(0, 0, 1);
toe.move(0, 2, 2);
toe.move(2, 2, 1);
toe.move(1, 1, 2);
toe.move(2, 0, 1);
toe.move(1, 0, 2); 
toe.move(2, 1, 1); 

