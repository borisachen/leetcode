951. Flip Equivalent Binary Trees
Medium/135/6


For a binary tree T, we can define a flip operation as follows: choose any node,
and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make
X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.
The trees are given by root nodes root1 and root2.


Example 1:
Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram

Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        t = self.dfs(root1, root2)
        return t

    def dfs(self, a, b):
        from collections import Counter
        if not a and not b: return True
        if not a or not b: return False
        if a.val != b.val: return False
        c1, c2 = [], []
        if a.left: c1.append(a.left.val)
        if b.left: c2.append(b.left.val)
        if a.right: c1.append(a.right.val)
        if b.right: c2.append(b.right.val)
        if Counter(c1) != Counter(c2): return False
        if a.left and not a.right and b.right and not b.left:
            b.left, b.right = b.right, b.left
        if not a.left and a.right and not b.right and b.left:
            b.left, b.right = b.right, b.left
        if not a.left and not a.right and not b.right and not b.left:
            return True
        if a.left and b.right and a.left.val == b.right.val:
            b.left, b.right = b.right, b.left
        l = self.dfs(a.left, b.left)
        r = self.dfs(a.right, b.right)
        if l and r: return True
        return False



public boolean flipEquiv(TreeNode r1, TreeNode r2) {
    if (r1 == null || r2 == null) return r1 == r2;
    if (r1.val != r2.val) return false;
    return flipEquiv(r1.left, r2.left) && flipEquiv(r1.right, r2.right) ||
        flipEquiv(r1.left, r2.right) && flipEquiv(r1.right, r2.left);
}
