988. Smallest String Starting From Leaf
Medium/74/5

Given the root of a binary tree, each node has a value from 0 to 25 representing
the letters 'a' to 'z': a value of 0 represents 'a', a value of 1 represents
'b', and so on.

Find the lexicographically smallest string that starts at a leaf of this tree
and ends at the root.

(As a reminder, any shorter prefix of a string is lexicographically smaller:
for example, "ab" is lexicographically smaller than "aba".  A leaf of a node is
a node that has no children.)



Example 1:
Input: [0,1,2,3,4,3,4]
Output: "dba"

Example 2:
Input: [25,1,3,1,3,0,2]
Output: "adz"

Example 3:
Input: [2,2,1,null,1,0,null,0]
Output: "abc"


Note:

The number of nodes in the given tree will be between 1 and 8500.
Each node in the tree will have a value between 0 and 25.
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        def dfs(node, path):
            if not node: return
            path.append(chr(ord('a')+node.val))
            if not node.left and not node.right:
                res[0] = min(res[0], ''.join(path)[::-1])
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            del path[-1]

        res = [str(chr(ord('z') + 1))]
        dfs(root, [])
        return res[0]


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.dfs(root, str(root.val), res)
        return self.convert(res[0])

    def dfs(self, node, temp, res):
        if not node:
            return
        if not node.left and not node.right:
            res.append(temp)
            if len(res) == 2:
                res = [res[0]] if res[0] < res[1] else [res[1]]
            return
        if node.left:
            self.dfs(node.left, str(node.left.val) + temp, res)
        if node.right:
            self.dfs(node.right, str(node.right.val) + temp, res)

    def convert(self, intstr):
        res = ''
        for i in intstr:
            res += chr(ord('a')+int(i))
        return res
