108. Convert Sorted Array to Binary Search Tree
Easy
882/95

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

-----
the array is sorted, so the middle element should be the root.
left half goes to left node, right half goes to right node

-----
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, len(nums)-1, nums)

    def helper(self, lo, hi, nums):
        if lo > hi: return None
        mid = lo + (hi - lo)//2
        node = TreeNode(mid)
        node.left = self.helper(lo, mid, nums)
        node.right = self.helper(mid+1, hi, nums)
        return node

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        half = int(len(nums)/2)
        node = TreeNode(nums[half])
        node.left = self.sortedArrayToBST(nums[0:half])
        node.right = self.sortedArrayToBST(nums[half+1:])
        return node
