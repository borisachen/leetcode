187. Repeated DNA Sequences 

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". 
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

1. use two sets, one for seen once, one for seen twice.
one pass.
o(n)

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        seen1 = set()
        seen2 = set()
        for i in range(len(s)-9):
        	word = s[i:i+10]
        	if word in seen1:
        		seen2.add(word)
        	else:
        		seen1.add(word)
        return list(seen2)