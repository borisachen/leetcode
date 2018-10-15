159. Longest Substring with At Most Two Distinct Characters

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.

----------
Two pointer apporach
dictionary to track elements in the current window
counter to track number of distinct characters in window
Time: O(n) since we are doing at most 2 passes
Space: O(1) since the dictionary is atleast 3.
----------

def longest(s):
	dic = {s[0]:1}
	count = 1
	i, j = 0,0
	n = len(s)
	res = 1
	while j < len(s):
		if count <= 2:
			j += 1
			if j > n-1: break
			if s[j] in dic:
				dic[s[j]] += 1
			else:
				dic[s[j]] = 1
				count += 1
		elif count > 2:
			if dic[s[i]] == 1:
				del dic[s[i]]
				count -= 1
			else:
				dic[s[i]] -= 1
			i += 1
		if count <= 2:
			res = max(res, j-i+1)
	print(res)

longest(s = 'eceba')
longest(s = 'baeeeccceeba')
