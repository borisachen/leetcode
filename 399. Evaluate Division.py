399. Evaluate Division
Medium/1113/91

Equations are given in the format A / B = k, where A and B are variables
represented as strings, and k is a real number (floating point number). Given
some queries, return the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values,
vector<pair<string, string>> queries , where equations.size() == values.size(),
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:

equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].
The input is always valid. You may assume that evaluating the queries will
result in no division by zero and there is no contradiction.

'''
Approach 1: Build a graph, then do BFS.

Approach 2: Modifed union find, where we keep track of the weight on each edge
'''

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = {}
        def build_graph(equations, values):
            def add_edge(a, b, val):
                if a in graph:
                    graph[a].append((b, val))
                else:
                    graph[a] = [(b, value)]
            for verticies, value in zip(equations, values):
                a, b = verticies
                add_edge(a, b, value)
                add_edge(b, a, 1 / value)
        def find_path(query):
            b, e = query
            if b not in graph and e not in graph:
                return -1.0
            q = collections.deque([(b, 1.0)])
            visited = set()
            while q:
                front, curproduct = q.popleft()
                if front == e:
                    return curproduct
                visited.add(front)
                for neighbor, value in graph[front]:
                    if neighbor not in visited:
                        q.append((neighbor, value * curproduct))
            return -1.0
        build_graph(equations,values)
        return [find_path(x) for x in queries]



class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        res = []
        parent = {}    # i.e. [a, b] then parent[a] = b
        weight = {}    # i.e. a / b = 2.0, then weight[a] = 2.0
        ufind = UnionFind(parent, weight)
        for i, edge in enumerate(equations):
            x1, x2 = edge[0], edge[1]
            val = values[i]
            if x1 not in parent and x2 not in parent:
                parent[x1] = x2
                parent[x2] = x2
                weight[x1] = val
                weight[x2] = 1
            elif x1 not in parent:
                parent[x1] = x2
                weight[x1] = val
            elif x2 not in parent:    # weight[x1] already exists, if make x2 be x1's parent. then weight[x1] will be overwrite.
                parent[x2] = x1
                weight[x2] = 1 / val
            else:
                ufind.union(x1, x2, val)

        for x1, x2 in queries:
            if x1 not in parent or x2 not in parent or ufind.find(x1) != ufind.find(x2):
                res.append(-1.0)
            else:
                factor1 = weight[x1]
                factor2 = weight[x2]
                res.append(factor1 / factor2)
        return res

class UnionFind():
    def __init__(self, parent, weight):
        self.parent = parent
        self.weight = weight

    def find(self, vertex):
        if self.parent[vertex] == vertex:
            return vertex
        root = self.find(self.parent[vertex])
        self.weight[vertex] *= self.weight[self.parent[vertex]]
        self.parent[vertex] = root
        return root

    def union(self, vertex1, vertex2, val):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        self.weight[root1]= self.weight[vertex2] * val / self.weight[vertex1]
        self.parent[root1] = root2
