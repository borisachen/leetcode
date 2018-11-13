247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

-----
We are trying to generate all sequences, so a backtracking type approach seems appropriate.
We recrusively generate solutions of length=targetlen.
for each result that we get back, we add 0,6,9,8,1 to the front and end of each string.

We can also do this iteratively:
first check if n is odd or even.
if even, start with empty string
if odd, start with 3 strings, 0,1,8
now we can use a queue like object and add the 5 options to each item in the queue.

-----

def strobo2(n):
	return helper(n, n)

def helper(targetlen, totallen):
	if targetlen == 0:
		return ['']
	if targetlen == 1:
		return ['0','1','8']
	sub = helper(targetlen-2, totallen)
	result = []
	for word in sub:
		if targetlen != totallen:
			result.append('0' + word + '0')
		result.append('1'+word+'1')
		result.append('6'+word+'9')
		result.append('9'+word+'6')
		result.append('8'+word+'8')
	return result

strobo2(3)


def strobo2_iterative(n):
	res = []
	if n % 2 == 0:
		res = ['']
	else:
		res = ['0','1','8']
	while n >= 2:
		temp = res
		res = []
		for word in temp:
			if n >= 4:
				res.append('0'+word+'0')
			res.append('1'+word+'1')
			res.append('6'+word+'9')
			res.append('9'+word+'6')
			res.append('8'+word+'8')
		n -= 2
	return res

strobo2_iterative(3)

