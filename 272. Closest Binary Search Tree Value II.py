272. Closest Binary Search Tree Value II

Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?

-----
Approach 1:
Iterate through all n nodes. Use MaxHeap of size K. 
O(nlogk)

Approach 2:
Find closest 1, remove it (logn)
Do this k times. O(klogn)
-----

import sys


class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def closest_bst_value_2(node, target, k):
	res = []
	for i in range(k):
		closest_val, closest_node, parent = find_closest_one(node, target)
		res.append(closest_val)
		node = remove(node, closest_val)
	return res


def find_closest_one(node, target):
	temp = node
	best_val = 0
	best_node = None
	best_dist = sys.maxint
	parent = None
	prev = None
	while temp:
		cand_dist = abs(temp.val - target)
		if cand_dist < best_dist:
			best_dist = cand_dist
			best_val = temp.val
			best_node = temp
			parent = prev
		if temp.left and target < temp.val:
			prev = temp
			temp = temp.left
		else: 
			prev = temp
			temp = temp.right
	return best_val, best_node, parent

head = Node(5)
head.left = Node(3)
head.left.left = Node(1)
head.left.right = Node(4)
head.right = Node(7)

find_closest_one(head, 2.7)
find_closest_one(head, 0.7)


def remove(head, node, parent):
	if node.left == None and node.right == None:
		
	# to remove a node, find the smallest node in the right subtree, and swap it with root.
	# in a BST, the smalles node is guaranteed to be the left most
	prev = None
	curr = node
	while curr.left:
		curr = curr.left
	# curr.left is None, so we swap values
	node.val = curr.val
	pass




