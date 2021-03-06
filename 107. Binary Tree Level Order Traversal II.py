107. Binary Tree Level Order Traversal II
Easy 578/98

Given a binary tree, return the bottom-up level order traversal of its nodes' values.
(ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
-----
This is the same as LC 102, we just need to invert the final list.
Iterative BFS with a queue.
-----

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q = [root]
        res = [[root.val]]
        while q:
            next = []
            tempres = []
            for node in q:
                if node.left:
                    next.append(node.left)
                    tempres.append(node.left.val)
                if node.right:
                    next.append(node.right)
                    tempres.append(node.right.val)
            res.append(tempres)
            q = next
        return res[:-1][::-1]
