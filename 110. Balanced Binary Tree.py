110. Balanced Binary Tree
Easy 936/85

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

-----
Bottom up DFS.
if L or R differ by more than 1, return -1.
else return 1 + the greater of L or R.
Time: O(n) since we visit each node once
Space: O(1) no additional storage
-----

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        x = self.help(root)
        return x!=-1

    def help(self, node):
        if not node:
            return 0
        l = self.help(node.left)
        r = self.help(node.right)
        if l==-1 or r==-1 or abs(l-r) > 1:
            return -1
        return max(l,r)+1
