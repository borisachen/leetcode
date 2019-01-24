205. Isomorphic Strings
Easy/632/177

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

-----
We can make a map from char1 -> char2.
Each char 1 should always map to the same char2.
This only checks for one to many mappings.
This doesn't check for many to one mappings,
but we can switch the strings and check the other one easily with a helper function.
Time O(n) to iterate over each string once, checking the map is O(1).
Space O(1) since we store every char we see but there is at most 256 ascii chars.
-----

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        return self.helper(s,t) and self.helper(t,s)

    def helper(self, s,t):
        m = {}
        for i in range(len(s)):
            for s[i] not in m:
                m[s[i]] = t[i]
            else:
                if m[s[i]] != t[i]:
                    return False
        return True
