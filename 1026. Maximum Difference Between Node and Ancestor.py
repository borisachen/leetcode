1026. Maximum Difference Between Node and Ancestor
Medium/686/29

Given the root of a binary tree, find the maximum value V for which there exists different nodes A and B where V = |A.val - B.val| and A is an ancestor of B.

(A node A is an ancestor of B if either: any child of A is equal to B, or any child of A is an ancestor of B.)

Example 1:

Input: [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: 
We have various ancestor-node differences, some of which are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.
 
Note:

The number of nodes in the tree is between 2 and 5000.
Each node will have value between 0 and 100000.

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        return self.helper(root, root.val, root.val)
    
    def helper(self, node, high, low):
        if not node:
            return high - low
        high = max(high, node.val)
        low = min(low, node.val)
        return max(self.helper(node.left, high, low), self.helper(node.right,high,low))


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, lo, hi):
        	# hi = largest value i've seen coming down from root to this node
        	# lo = smallest value seen from root to this node
            if not node:
                return hi - lo
            lo = min(node.val, lo)
            hi = max(node.val, hi)
            R = dfs(node.right, lo, hi)
            L = dfs(node.left, lo, hi)
            return max(L, R)
        return dfs(root, root.val, root.val)