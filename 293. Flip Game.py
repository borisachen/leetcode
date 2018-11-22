293. Flip Game

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].

-----
We should be able to do this in one pass.
for each i, if i and i+1 are the same sign and both '+', then we can flip those, add it to res.
Time: O(n)

Notes:
- strings are not mutable so we need to turn it into a list or array
-----


def flip_game(s):
	sa = [x for x in s]
	d = {'+':'-'}
	res = []
	for i in range(len(s)-1):
		if s[i] == s[i+1] and s[i] == '+':
			sa[i] = '-'
			sa[i+1] = '-'
			res.append(''.join(sa))
			sa[i] = '+'
			sa[i+1] = '+'
	print(res)


flip_game(s = '++++')