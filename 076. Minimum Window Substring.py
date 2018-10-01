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


class Solution(object):
    def minWindow(self, string, target):
        """
        :type string: str
        :type target: str
        :rtype: str
        """
        # counter represents the number of chars of t to be found in s
        target_map = collections.Counter(target)
        count = len(target)
        start = end = head = 0
        min_substring_length = sys.maxsize
        # Move end to find a valid window.
        while end < len(string):
            #if character doesn't exist in map it returns 0
            if target_map[string[end]] > 0:
                count -= 1
            target_map[string[end]] -= 1
            end += 1
            # When we found a valid window, move start to find smaller window.
            while count == 0:
                if (end - start) < min_substring_length:
                    min_substring_length = end - start
                    head = start
                target_map[string[start]] += 1
                # When char exists in target, increase counter.
                if target_map[string[start]] >0:
                    count += 1
                start += 1
        return "" if min_substring_length == sys.maxsize else string[head:head + min_substring_length]
