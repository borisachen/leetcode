105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

the first element of preorder is the root. suppose it is 5
then we find 5 in the inorder list, say it is in index j.
	everything to the left of 5 will be in the left node.
		prestart = preStart+1
		instart = inStart
		inend = j-1
	everything to the right of 5 will be in the right node.
		instart = j +1
		inend = inend
		prestart = preStart+1+j


class Solution(object):
	def buildTree(self, preorder, inorder):
		"""
		:type preorder: List[int]
		:type inorder: List[int]
		:rtype: TreeNode
		"""
		return self.build(0, 0, len(inorder)-1, preorder, inorder)

	def build(self, prestart, instart, inend, preorder, inorder):
		if prestart > len(preorder) or instart > inend:
			return None
		node = TreeNode(preorder[prestart])
		j=instart
		for i in range(instart, inend+1):
			if inorder[i]==node.val:
				j = i
		node.left = self.build(prestart+1, instart, j-1, preorder, inorder)
		node.right = self.build(prestart+j-instart+1, j+1, inend, preorder, inorder)
		return node











Hi guys, this is my Java solution. I read this post, which is very helpful.

The basic idea is here:
Say we have 2 arrays, PRE and IN.
Preorder traversing implies that PRE[0] is the root node.
Then we can find this PRE[0] in IN, say its IN[5].
Now we know that IN[5] is root, so we know that IN[0] - IN[4] is on the left side, IN[6] to the end is on the right side.
Recursively doing this on subarrays, we can build a tree out of it :)

Hope this helps.

public TreeNode buildTree(int[] preorder, int[] inorder) {
    return helper(0, 0, inorder.length - 1, preorder, inorder);
}

public TreeNode helper(int preStart, int inStart, int inEnd, int[] preorder, int[] inorder) {
    if (preStart > preorder.length - 1 || inStart > inEnd) {
        return null;
    }
    TreeNode root = new TreeNode(preorder[preStart]);
    int inIndex = 0; // Index of current root in inorder
    for (int i = inStart; i <= inEnd; i++) {
        if (inorder[i] == root.val) {
            inIndex = i;
        }
    }
    root.left = helper(preStart + 1, inStart, inIndex - 1, preorder, inorder);
    root.right = helper(preStart + inIndex - inStart + 1, inIndex + 1, inEnd, preorder, inorder);
    return root;
}
