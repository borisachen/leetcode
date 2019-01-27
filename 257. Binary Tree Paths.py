257. Binary Tree Paths
Easy/714/60

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.res = []
        if not root:
            return []
        self.help(root, [str(root.val)])
        return self.res
    def help(self, node, path):
        if not node.left and not node.right:
            self.res.append('->'.join(path))
            return
        if node.left:
            self.help(node.left, path+[str(node.left.val)])
        if node.right:
            self.help(node.right, path+[str(node.right.val)])
        return

# dfs + stack
def binaryTreePaths1(self, root):
    if not root:
        return []
    res, stack = [], [(root, "")]
    while stack:
        node, ls = stack.pop()
        if not node.left and not node.right:
            res.append(ls+str(node.val))
        if node.right:
            stack.append((node.right, ls+str(node.val)+"->"))
        if node.left:
            stack.append((node.left, ls+str(node.val)+"->"))
    return res
    
