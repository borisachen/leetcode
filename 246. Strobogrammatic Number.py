246. Strobogrammatic Number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

-----
The only numbers that are relevant are
1,6,8,9,0
1,8,0 can be anywhere
6 needs to be complimented by 9 in the mirror image.
How do we check for the mirror image 6-9s?
Compute mid.
If len is odd, then if there is a 6 at (mid-i), then (mid+i) must be a 9
If len is even, then if there is a 6 at i, then () must be a 9

There is a simple way: take the first half of the query and invert it.
replace 6 with 9 and 9 with 6.
then check if the invert is the same as the second half.
-----


query = '818'

def doit(query):
	d = {'0':'0',
		'1':'1',
		'8':'8',
		'6':'9',
		'9':'6'}
	i=0
	j=len(query)-1
	while i <= j:
		f = query[i]
		b = query[j]
		if f in d and b in d and d[f] == b:
			i += 1
			j -= 1
		else:
			return False
	return True

doit(query)