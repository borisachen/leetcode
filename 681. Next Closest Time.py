681. Next Closest Time

Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned

------------------------------
Naively:
- We could generate all possible permutations with backtracking.
- Then do one pass to find the closest one.

Improvements:
- Well we know that we want to change as few of the upfront digits as possible for rounding down.
- For rounding up, not sure there is a systematic way.
------------------------------

# Count time forward 
class Solution(object):
	def nextClosestTime(self, time):
		cur = 60 * int(time[:2]) + int(time[3:])
		allowed = {int(x) for x in time if x != ':'}
		while True:
			cur = (cur + 1) % (24 * 60)
			if all(digit in allowed
				for block in divmod(cur, 60) 
				for digit in divmod(block, 10)):
				return "{:02d}:{:02d}".format(divmod(curr, 60))

# build from allowed digits
class Solution(object):
	def nextClosestTime(self, time):
		ans = start = 60 * int(time[:2]) + int(time[3:])
		elapsed = 24 * 60
		allowed = {int(x) for x in time if x != ':'}
		for h1, h2, m1, m2 in itertools.product(allowed, repeat=4)
			hours = 10 * h1 + h2
			mins = 10 * m1 + m2
			if hours < 24 and mins < 60:
				cur = 60 * hours + mins
				cand_elapsed = (cur - start) % (24 * 60)
				if 0 < cand_elapsed < elapsed:
					ans = cur
					elapsed = cand_elapsed
		return "{:02d}:{:02d}".format(*divmod(ans, 60))





S = '19:34'

# First collect all the unique digits
digits = []
for char in S:
	if char not in digits and char != ':':
		digits.append(char)

# Now backtrack go generate all the possibilities


def backtrack(temp, res, S):
	if len(temp) == len(S):
		res.append(temp)
		return
	for i in range(len(S)):
		backtrack(temp+S[i], res, S)

res = []
backtrack('', res, '1934')

# Now res is populated with all possibilities, so we just need a function to compute the distance to the target
query = '1111'

def distance(query, target):
	if int(query[0:2]) > 24 or int(query[2:4]) > 60:
		return -1
	minutes1 = int(query[0:2]) * 60 + int(query[2:4])
	minutes2 = int(target[0:2]) * 60 + int(target[2:4])
	a = abs(minutes1 - minutes2)
	b = abs(minutes1 + 24*60 - minutes2)
	c = abs(minutes1 - (minutes2 + 24*60))
	return min([a,b,c])


target = S[0:2] + S[3:5]
dist_list = [distance(x, target) for x in res]










