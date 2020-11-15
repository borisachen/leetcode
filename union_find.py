from collections import defaultdict

class Graph:
	def __init__(self, num_of_v):
		self.num_of_v = num_of_v
		self.edges = defaultdict(list)

	def add_edge(self, u, v):
		self.edges[u].append(v)

class Subset:
	def __init__(self, parent, rank):
		self.parent = parent
		self.rank = rank

# find the parent of a node, w/path compression
def find(subsets, node):
	if subsets[node].parent != node:
		subsets[node].parent = find(subsets, subsets[node].parent)
	return subsets[node].parent

def union(subsets, u, v):
	# attach smaller rank tree under root of higher rank tree
	if subsets[u].rank > subsets[v].rank:
		subsets[v].parent = u
	elif subsets[v].rank > subsets[u].rank:
		subsets[u].parent = v
	# if ranks are the same, then make one as the root and up its rank by 1
	else:
		subsets[v].parent = u
		subsets[u].rank += 1

def isCycle(graph):
	subsets = []
	for u in range(graph.num_of_v):
		subsets.append(Subset(u,0))
	for u in graph.edges:
		u_rep = find(subsets, u)
		for v in graph.edges[u]:
			v_rep = find(subsets, v)
			if u_rep == v_rep:
				return True
			else:
				union(subsets, u_rep, v_rep)

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)

if isCycle(g):
	print('graph contains cycle')
else:
	print('no cycle')
