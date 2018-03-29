98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the nodes key.
The right subtree of a node contains only nodes with keys greater than the nodes key.
Both the left and right subtrees must also be binary search trees.
"""
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        import sys
        return self.validnode(root, -sys.maxint, sys.maxint)
    def validnode(self, node, lo, hi):
        if not node:
            return True
        if node.val >= hi or node.val <= lo:
            return False
        left = self.validnode(node.left, lo, node.val)
        right = self.validnode(node.right, node.val, hi)
        return (left & right)








# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root: return True
    a,b = self.helper(root)
    return b

  def helper(self, node):
    if not node:
      return [], True
    left_list, left_bool = self.helper(node.left)
    right_list, right_bool = self.helper(node.right)
    if not left_bool or not right_bool:
      return [], False
    node_is_bst = True
    for left_item in left_list:
      if not left_item < node.val: 
        node_is_bst = False
        break
    for right_item in right_list:
      if not right_item > node.val: 
        node_is_bst = False
        break
    val_list = left_list + [node.val] + right_list
    return val_list, node_is_bst


class Solution(object):
  def isValidBST(self, root):
    import sys
    return self.isValidNode(root, -sys.maxint - 1, sys.maxint)

  def isValidNode(self, node, lo, hi):
    if not node: return True
    if node.val >= hi or node.val <= lo: return False
    return self.isValidNode(node.left, lo, node.val) and self.isValidNode(node.right, node.val, hi)



public class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    public boolean isValidBST(TreeNode root, long minVal, long maxVal) {
        if (root == null) return true;
        if (root.val >= maxVal || root.val <= minVal) return false;
        return isValidBST(root.left, minVal, root.val) && isValidBST(root.right, root.val, maxVal);
    }
}





