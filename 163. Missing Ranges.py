163. Missing Ranges

Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].

-------------------------
Approach 1:
res = []
for i in lower...upper:
	temp = []
	if i in given, then reset temp and res.append(temp)
	else temp += i
At the end of this, we have a list of lists, giving us the ranges.
We dont need all the items in temp, just the first and last.
So we can add the first and only add the last, which we know is the last since there is an if considiton.

if n = len(given), m = upper, time complexity is O(n*m)
We can improve by using a hashmap for given -> O(m + n)

Approach 2:
Consider each pair at a time. 
We can generate the the list for each pair.
Append lower to the beginning and upper to the end.

-------------------------

given = [0, 1, 3, 50, 75]
lower = 0
upper = 99

def missing_ranges(given, lower, upper):
	g2 = [lower-1] + given + [upper+1]
	res = []
	for i in range(len(g2)-1):
		lo = g2[i]
		hi = g2[i+1]
		temp = ''
		if hi - lo > 2:
			temp = "%s->%s" % (lo+1, hi-1)
		if hi - lo == 2:
			temp = str(hi - 1)
		if temp != '':
			res.append(temp)
	return res

missing_ranges(given = [0, 1, 3, 50, 75], lower = 0, upper = 99)
