3. Longest Substring Without Repeating Characters
<<<<<<< HEAD
Medium/8629/522
=======
Medium/6944/411
>>>>>>> 58ee1fb8f704abd4334680bea0009785ad68ddfd

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""]]]
Rolling window .

keep a hashmap which stores the characters in string as keys and their positions as values,
keep two pointers which define the max substring. j, i
move the right pointer to scan through the string: i
and meanwhile update the hashmap.
If the character is already in the hashmap,
    then move the left pointer to the right of the same character last found.
Note that the two pointers can only move forward.
"""

class Solution(object):
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
        d = set()
        j = 0
        res = 0
        for i in range(len(s)):
            if s[i] not in d:
                d.add(s[i])
                res = max(res, len(d))
            else:
                while s[i] in d:
                    d.remove(s[j])
                    j += 1
                d.add(s[i])
        return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
          i
        pwwkew
          j
            keep a hashmap which stores the characters in string as keys and their positions as values,
            keep two pointers which define the max substring. j, i
            move the right pointer to scan through the string: i
            and meanwhile update the hashmap.
            If the character is already in the hashmap,
                then move the left pointer to the right of the same character last found.
            Note that the two pointers can only move forward.
        """
        if len(s)==0:
            return 0
        d = {}
        maxx = 0
        j = 0
        for i in range(0, len(s)):
            if s[i] in d:
                j = max(j, d[s[i]]+1)
            d[s[i]] = i
            maxx = max(maxx, i-j+1)
        return maxx

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if len(s == 0): 
            return 0
        d = {}
        maxx = 0
        j = 0
        for i in range(0, len(s)):
            if s[i] in d:
                j = max(j, d[s[i]] + 1):
            d[s[i]] = i
            maxx = max(maxx, i - j + 1)
        return maxx