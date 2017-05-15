150. Evaluate Reverse Polish Notation
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

1. use a stack,
whenever we see a non numeric, pop the last two, do the operation, push the result

class Solution(object):
	def evalRPN(self, tokens):
		"""
		:type tokens: List[str]
		:rtype: int
		"""
		stack = []
		for i in tokens:
			if i not in ['+','-','/','*']:
				stack.append(int(i))
			else:
				a = stack.pop()
				b = stack.pop()
				if i=='+': stack.append(b+a)
				elif i=='-': stack.append(b-a)
				elif i=='*': stack.append(b*a)
				else: 
					if a*b < 0 and b%a !=0: stack.append(b/a+1)
					else: stack.append(b/a)
		return stack[0]

	def isint(self, n):
		try:
			int(n)
			return True
		except ValueError:
			return False