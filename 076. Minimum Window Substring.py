76. Minimum Window Substring
DescriptionHintsSubmissionsDiscussSolution
Pick One
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.


class Solution(object):
	def minWindow(self, s, t):
		"""
		:type s: str
		:type t: str
		:rtype: str
		"""
		need = collections.Counter(t)
		missing = len(s)
		i = I = J = 0
		for j, c in enumerate(s, 1): # for each character in s
			if need[c] > 0: # if i still need this character,
				missing -= 1  # then subtract one from missing since we found a missing char
			need[c] -= 1 # subtract one from needing [c]
			if missing == 0: # if we aren't missing any chars:
				while i < j and need[s[i]] < 0: # while the beginning char, s[i], is still a character we have excess of (need[s[i]] < 0)
					need[s[i]] += 1 # add one since we observe that char here
					i += 1 # move left pointer up
				if not J or i-j <= J-I: # if we have no result (J==0), or if the current result is shorter than the best result
					I, J = i, j # update the best result pointers, I and J
		return s[I:J]

