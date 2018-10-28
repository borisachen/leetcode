270. Closest Binary Search Tree Value

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

---
---
# Recursive approach
def closest_in_bst(node, target):
	best_val = 0
	best_diff = sys.maxint
	def dfs(node, target):
		if not node: return
		if abs(node.val-target) < best_diff:
			best_diff = abs(node.val - target)
			best_val = node.val
		if node.val > target and node.left:
			dfs(node.left)
		if node.val < target and node.right:
			dfs(node.right)
		return
	dfs(node, target)
	return best_val

# Iterative

def closest_in_bst(node, target):
	curr = node
	best_diff = sys.maxint
	best_val = 0
	while curr:
		if abs(curr.val-target) < best_diff:
			best_diff = abs(curr.val - target)
			best_val = curr.val
		if target > curr.val:
			curr = curr.right
		elif target < curr.val:
			curr = curr.left
		else:
			return curr.val
	return best_val
