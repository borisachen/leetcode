67. Add Binary
Easy

754

153

Favorite

Share
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

-----
Approach 1, stay in binary, carry 1 each time
0 pad the shorter sequence
-----
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0 or j >= 0:
            sum0 = carry
            if i >= 0: sum0 += int(a[i])
            if j >= 0: sum0 += int(b[j])
            i -= 1
            j -= 1
            res += str(sum0%2)
            carry = sum0//2
        if carry != 0: res += str(carry)
        return res[::-1]
