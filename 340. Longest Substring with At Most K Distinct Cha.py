340. Longest Substring with At Most K Distinct Characters

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.

-------------------------
We should be able to do a 2 pointer sliding window approach.
A hashmap can track the current count of all characters in the window.
if current counter is > k, we should move the left pointer
	decrease the dictionary, if its 0 for this char, then delete the key and lower counter
	until count <= k
if current counter is < k, we should move the right pointer
	if char already exists:
		increase the dictionary at [char]
	else:
		add dic[char] = 1 to the dictionary
		incerase the counter

Complexity:
At each step, the dictionary look ups are O(1), and we are only making one pass with each pointer,
So Time Complexity is O(n)
Space complexity: worst case we are storing all characters in the dictinoary, so O(n)
-------------------------

s = 'eceba'
k = 2

def longest(s, k):
	d = {s[0]:1}
	count = 1
	left = 0
	right = 0
	best = 0
	best_l, best_r = 0, 0
	while right < len(s):
		print(left, right, count, d)
		if count <= k:
			right += 1
			if right < len(s):
				if s[right] in d:
					d[s[right]] += 1
				else:
					d[s[right]] = 1
					count += 1
		elif count > k:
			left += 1
			d[s[left-1]] -= 1
			if d[s[left-1]] == 0:
				del d[s[left-1]]
				count -= 1
		if count <= k:
			if max(best, right-left) > best:
				best = max(best, right-left)
				best_l, best_r = left, right
	return s[best_l:best_r+1]

longest('eceba', 2)
longest('beeceeba', 2)
longest("aabbcc", k = 1)
longest("aabbcc", k = 2)
longest("aabbcc", k = 3)
longest("aaabbb", k = 3)