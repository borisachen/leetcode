241. Different Ways to Add Parentheses 

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]

class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit(): return [int(input)]
        res = []
        n = len(input)
        for i in range(n):
        	if input[n] in "-+*":
        		res1 = self.diffWaysToCompute(input[:i])
        		res2 = sefl.diffWaysToCompute(input[i+1:])
        		for j in res1:
        			for k in res2:
        				res.append(self.helper(j, k, input[i]))
    def helper(j, k, sym):
    	if op == '+': return j+k
    	if op == '*': return j*k
    	if op == '-': return j-k