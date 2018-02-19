94. Binary Tree Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Iterative
use a stack and a pointer
go left, pushing onto the stack, until we hit null
	pop, add the val,
	push the righ one
repeat while stack is not empty or root is not null

class Solution(object):
	def inorderTraversal(self, root):
		if not root: return []
		res = []
		stack = []
		cur = root
		while cur or stack:
			while cur:
				stack.append(cur)
				cur = cur.left
			cur = stack.pop()
			res.append(cur.val)
			stack.append(cur.right)
		return res




# Iterative

class Solution(object):
	def inorderTraversal(self, root):
		if not root: return []
		stack = []
		res = []
		cur = root
		while stack or cur:
			while cur:
				stack.append(cur)
				cur = cur.left
			cur = stack.pop()
			res.append(cur.val)
			cur = cur.right
		return res


public List<Integer> inorderTraversal(TreeNode root) {
    List<Integer> list = new ArrayList<Integer>();

    Stack<TreeNode> stack = new Stack<TreeNode>();
    TreeNode cur = root;

    while(cur!=null || !stack.empty()){
        while(cur!=null){
            stack.add(cur);
            cur = cur.left;
        }
        cur = stack.pop();
        list.add(cur.val);
        cur = cur.right;
    }

    return list;
}


class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root: return []
		res = []
		self.helper(root, res)
		return res

	def helper(self, node, res):
		if node.left:
			self.helper(node.left, res)
		res.append(node.val)
		if node.right:
			self.helper(node.right, res)
		return



class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root: return []
		res = []
		self.dfs(node, res)
		return res

	def dfs(self, node, res):
		if node.left:
			self.dfs(node.left)
		res.append(node.val)
		if node.right
			self.dfs(node.right)
		return



class Solution(object):
	def inorderTraversal(self, root):
		"""
		:type root: TreeNode
		:rtype: List[int]
		"""
		if not root: return []
		res = []
		stack = [root]
		curr = root
		while stack:
			while curr.left:
				stack.append(curr)
				curr = curr.left
			cur = stack.pop()
			res.append(cur.val)
			cur = cur.right
