1028. Recover a Tree From Preorder Traversal
Hard/533/21

We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

 

Example 1:
Input: "1-2--3--4-5--6--7"
Output: [1,2,5,3,4,6,7]

Example 2:
Input: "1-2--3---4-5--6---7"
Output: [1,2,5,3,null,6,null,4,null,7]
 
Example 3:
Input: "1-401--349---90--88"
Output: [1,401,null,349,88,90]

"""
Explanation
We save the construction path in a stack.
In each loop,
we get the number level of '-'
we get the value val of node to add.

If the size of stack is bigger than the level of node,
we pop the stack until it's not.

Finally we return the first element in the stack, as it's root of our tree.

Complexity
Time O(S), Space O(N)
"""

def recoverFromPreorder(self, S):
	stack = []
	i = 0
    while i < len(S):
    	level = 0
    	val = ""
        while i < len(S) and S[i] == '-':
        	level += 1
        	i +=  1
        while i < len(S) and S[i] != '-':
        	val += S[i]
        	i += 1
            #val, i = val + S[i], i + 1
        while len(stack) > level:
            stack.pop()
        node = TreeNode(val)
        if stack and stack[-1].left is None:
            stack[-1].left = node
        elif stack:
            stack[-1].right = node
        stack.append(node)
    return stack[0]