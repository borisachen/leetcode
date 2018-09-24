261. Graph Valid Tree

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected, 
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

------------------------------------
Valid tree means: 
- There are no dangling nodes. Every node is at least in one edge
- No cycle.
- There every node is connected to every other 
If this is all, then we can check each condition independently.
To check for cycles, we keep a visited set of nodes.
For each node, do a DFS search and if we come back to visited node, then there is a cycle.
------------------------------------

n=5
edges = [[0, 1], [0, 2], [0, 3], [1, 4]]

# preprocess edges into a dictionary?
def graph_valid_tree(edges, n):
	from collections import defaultdict
	graph = defaultdict(list)
	visited = [False] * n
	for e in edges:
		graph[e[0]].append(e[1])
		graph[e[1]].append(e[0])
	def dfs_is_cycle(node, visited, parent):
		visited[node] = True
		for child in graph[node]:
			if visited[child] == False:
				if dfs_is_cycle(child, visited, parent=node):
					return True
			elif child != parent:
				return True
		return False
	if dfs_is_cycle(0, visited, -1) == True:
		return False
	for i in range(n):
		if visited[i] == False:
			return False
	return True

graph_valid_tree(edges = [[0, 1], [0, 2], [0, 3], [1, 4]], n=5)
graph_valid_tree(edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], n=5)

