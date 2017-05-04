133. Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJs undirected graph serialization:
Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
Visually, the graph looks like the following:
"""
       1
      / \
     /   \
    0 --- 2
         / \
         \_/
"""
# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

1. start by copying the head node
use a stack to store what nodes to visit next
use a dict to store what nodes weve seen.
	key = node.val`
	value = the node itself
visit 1st node, push onto stack
while the stack still has nodes:
	pop
	for each neighboring node, check if we have seen it before
	if not, then push onto stack.
	if yes, then continue to next on stack



class Solution(object):
	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):
		if not node: return node
		seen = {}
		head = UndirectedGraphNode(node.label)
		seen[node.label] = head
		stack = [node]
		while stack:
			top = stack.pop()
			for neighb in top.neighbors:
				if neighb.label not in seen:
					stack.append(neighb)
					seen[neighb.label] = UndirectedGraphNode(neighb.label)
				seen[top.label].neighbors.append(seen[neighb.label])
		return head














