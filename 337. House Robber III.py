337. House Robber III
Medium/1210/27

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \ 
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
-----
Approach 1:
for each node, we can rob it or not rob it. what we pass up depends only on looking two levels down.
Since this is exponential in time, we can use a dictionary to cache seen nodes.

Approach 2:
split each rob_helper into two return values:
a = if node is robbed
b = if node is not robbed
-----
# Definition for a binary tree root.
# class Treeroot:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Approach 1
class Solution:
    def rob(self, root):
        d = {}
        return self.help(root, d)
    def help(self, root, d):
        """
        :type root: Treeroot
        :rtype: int
        """
        if not root: 
            return 0
        if root in d:
            return d[root]
        a = root.val
        b = 0
        if root.left: 
            a += self.help(root.left.left, d) + self.help(root.left.right, d)
            b += self.help(root.left,d)
        if root.right: 
            a += self.help(root.right.left,d) + self.help(root.right.right,d)
            b += self.help(root.right,d)
        res = max(a,b)
        d[root] = res
        return res

# Approach 2

class Solution:
	def rob(self, root):
		res = self.robhelp(root)
		return max(res[0], res[1])
	def robhelp(self, node):
		if not node: return [0,0]
		l = self.robhelp(node.left)
		r = self.robhelp(node.right)
		a = node.val + l[1] + r[1]
		b = max(l[0],l[1]) + max(r[0],r[1])
		return [a,b] # a = rob node, b = DONT rob node
