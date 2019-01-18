168. Excel Sheet Column Title
Easy 596/118

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
-----
We are essential changing the number to base 26.
A   1     AA    26+ 1     BA  2×26+ 1     ...     ZA  26×26+ 1     AAA  1×26²+1×26+ 1
B   2     AB    26+ 2     BB  2×26+ 2     ...     ZB  26×26+ 2     AAB  1×26²+1×26+ 2
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............   
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
.   .     ..    .....     ..  .......     ...     ..  ........     ...  .............
Z  26     AZ    26+26     BZ  2×26+26     ...     ZZ  26×26+26     AAZ  1×26²+1×26+26

Note there is a issue with the 1 indexing above. 
Z:  26 % 26 = 0 but we want 25, so we take (n-1) % 26 instead
A:   1 % 26 = 1, but we want 0.
AA: 27 % 26 = 1, and again we want 0.
-----

class Solution:
	def convertToTitle(self, n):
		"""
		:type n: int
		:rtype: str
		"""
		d = {}
		for i in range(97, 97+26):
			d[i-97] = chr(i).upper()
		res = ''
		while n > 0:
			div = (n-1) // 26	
			remain = (n-1) % 26
			res = d[remain] + res
			n = div
		return res