144. Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

1. recursive:
base case, if node is null, return and do nothing
add the node val to res
call left,
call right

2. iterative
stack


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            top = stack.pop()
            res.append(top.val)
            if top.right: stack.append(top.right)
            if top.left: stack.append(top.left)
        return res



class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if not node: return
        res.append(node.val)
        self.helper(node.left, res)
        self.helper(node.right, res)



