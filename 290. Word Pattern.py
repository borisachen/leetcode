290. Word Pattern
Easy/520/58

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern and not str:
            return True
        if not pattern or not str:
            return False
        d = {}
        d2={}
        words = str.split(' ')
        seen = set()
        if len(pattern) != len(words):
            return False
        for i,char in enumerate(pattern):
            word = words[i]
            if char not in d and word not in d2:
                d[char]=i
                d2[word]=i
            elif char not in d or word not in d2:
                return False
            else:
                if d[char] != d2[word]:
                    return False
                d[char]=i
                d2[word]=i
        return True
