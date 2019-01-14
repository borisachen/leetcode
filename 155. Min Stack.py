155. Min Stack
Easy 1405/153

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

-----
-----

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []

    def push(self, x):
        """
        :type x: int
        :rtrype: void
        """
        curmin = self.getMin()
        if curmin == None or x < curmin:
            curmin = x
        self.s1.append((x, curmin))

    def pop(self):
        """
        :rtype: void
        """
        if not self.s1: return
        self.s1.pop()

    def top(self):
        """
        :rtype: int
        """
        if not self.s1: return None
        return self.s1[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.s1: return None
        return self.s1[-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
