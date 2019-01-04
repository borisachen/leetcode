842. Split Array into Fibonacci Sequence

Given a string S of digits, such as S = "123456579", we can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list F of non-negative integers such that:

0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
F.length >= 3;
and F[i] + F[i+1] = F[i+2] for all 0 <= i < F.length - 2.
Also, note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from S, or return [] if it cannot be done.

Example 1:

Input: "123456579"
Output: [123,456,579]
Example 2:

Input: "11235813"
Output: [1,1,2,3,5,8,13]
Example 3:

Input: "112358130"
Output: []
Explanation: The task is impossible.
Example 4:

Input: "0123"
Output: []
Explanation: Leading zeroes are not allowed, so "01", "2", "3" is not valid.
Example 5:

Input: "1101111"
Output: [110, 1, 111]
Explanation: The output [11, 0, 11, 11] would also be accepted.
Note:

1 <= S.length <= 200
S contains only digits.

---------------------------
Naively we could search every possible combination in a greedy like fashion via backtracking

try all adding all permuations of s[idx:i] for i in [idx, n]
- no leading zero: if s[idx]=='0' and i >
---------------------------

def split_array_into_fib(s):
	temp = []
	backtrack(s, temp, 0)
	return temp

def backtrack(s, temp, idx):
	if idx == len(s) and len(temp) >= 3:
		return True
	for i in range(idx, len(s)):
		if s[idx] == '0' and i > idx:
			break
		num = int(s[idx:i+1])
		size = len(temp)
		if size >= 2 and num > temp[-1] + temp[-2]:
			break
		if size <= 1 or num == temp[-1] + temp[-2]:
			temp.append(int(num))
			if backtrack(s, temp, i+1): return True
			temp.pop()
	return False

split_array_into_fib("123456579")
split_array_into_fib("11235813")
split_array_into_fib("112358130")
split_array_into_fib("1101111")
