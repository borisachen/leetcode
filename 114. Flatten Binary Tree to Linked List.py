114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given
"""
         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
"""
go down the left
stop when we get to the bottom left, call in A
continue in order traversal, and continue to append to the left
once we are done, switch everything to the right

better recursive:
create a pointer to left and right
set node.left to null
flatten the copy of left
flatten the copy of right
set node.right = flattened left, because the left side should go first
then we need to find the end of the path we just appended.
set cur = node, then iterate to the right child until we hit the end
once we find the end, set the right child to the right copy



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
  def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if not root: return None
    left = root.left
    right = root.right
    node.left = None
    self.flatten(left)
    self.flatten(right)
    node.right = left
    temp = node
    while temp.right: temp = temp.right
    temp.right = right



















class Solution(object):
  def flatten(self, root):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if not root: return None
    left = root.left
    right = root.right
    root.left = None
    self.flatten(left)
    self.flatten(right)
    root.right = left
    cur = root
    while cur.right:
      cur = cur.right
    cur.right = right




