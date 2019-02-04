979. Distribute Coins in Binary Tree
Medium/179/3

Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Example 1:

Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.

Example 2:
Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.

Example 3:
Input: [1,0,2]
Output: 2

Example 4:
Input: [1,0,0,null,3]
Output: 4
-----
Approach 1: from each node, with the result of the left and right children,
we can compute the cost so far based on how many coins we've seen.
Time: O(n) where n = number of nodes
Space: O(1) since we dont use any extra storage
-----
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ca, co = self.help(root)
        return co

    def help(self, node):
        if not node: return 0,0
        l1, l2 = self.help(node.left)
        r1, r2 = self.help(node.right)
        carry = l1 + r1 + node.val - 1
        cost = l2 + r2 + abs(carry)
        return carry, cost
