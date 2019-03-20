101. Symmetric Tree
Easy/1734/36

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
-----

Approach 2:
Recursive, need L and R.
Check L.val == R.val
then check help(L.L, R.R) == True and help(L.R, R.L) == True

Approach 1:
BFS, check each level is symmetric

-----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        if not root: return True
        return self.helper(root.left, root.right)
    def helper(self, left, right):
        if not left and not right: return True
        if not left or not right: return False
        return left.val==right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        stack = [(root.left, root.right)]
        while stack:
            l, r = stack.pop(0)
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val == r.val:
                stack.append((l.left, r.right))
                stack.append((l.right, r.left))
            else:
                return False
        return True
