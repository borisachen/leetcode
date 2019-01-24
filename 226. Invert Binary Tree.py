226. Invert Binary Tree
Easy/1380/24

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

-----
-----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        l = self.invertTree(root.left)
        r = self.invertTree(root.right)
        root.left = r
        root.right = l
        return root

# Iterative Stack/queue DFS/BFS
class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        s = [root]
        while s:
            node = s.pop() # for stack
            #node = s.pop(0) for queue
            node.left, node.right = node.right, node.left
            if node.left:
                s.append(node.left)
            if node.right:
                s.append(node.right)
        return root
