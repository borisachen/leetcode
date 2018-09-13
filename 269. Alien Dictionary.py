269. Alien Dictionary

There is a new alien language which uses the latin alphabet. 
However, the order among letters are unknown to you. 
You receive a list of non-empty words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

Thoughts:
In the example, we can derive:
- t < f 
- w < e < r < t
We get here by comparing each pair of subsequent words.
- Within each comparison, we step through both words at the same time,
- and look for the first pair of characters that don't mach
- this implies an ordering of those two characters

Strategy:
To keep track of the ordering of characters as we discover them, we need some data structure.
Assigning scalar/numeric values to characters is a first through, but then the values would have to be adjusted, which is not ideal.
A better structure would be a directed acyclic graph, where each edge represents an ordering between the characters.

Given the graph, we just need to find a topological ordering.
- We will use a modified depth first search with a set and a stack
- the set will store all the nodes we have seen
- the stack will store current node in topological order
- while there are any unvisited nodes,
  - pick a random node to visit
  - perform DFS search on that node.
  - when a node has no children, we add it to the stack.
  - this guarantees that the nodes at the bottom of the stack are at the bottom of the ordering
- once we have visited all nodes, pop of all items in the stack to obtain a topological ordering.


dictionary = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

def alien_dictionary():
  # initialize the graph with all the characters
  graph = {}
  for word in dictionary:
    for char in word:
      if char not in graph:
        graph[char] = []

  # iterate through dictionary and compare word1 vs word2, fill the edges of the graph
  for i in range(len(dictionary)-1):
    word1 = dictionary[i]
    word2 = dictionary[i+1]
    m = min(len(word1), len(word2))
    for j in range(m):
      if word1[j] != word2[j] and word2[j] not in graph[word1[j]]:
        graph[word1[j]].append(word2[j])

  # given graph, find a topological ordering.
  visited = set() 
  stack = []

  def dfs(node, graph):
    print ('dfs(%s)' % node)
    count = 0
    for child in graph[node]:
      if child in visited:
        count += 1
    if count == len(graph[node]):
      visited.add(node)
      stack.append(node)
      return 
    visited.add(node)
    for child in graph[node]:
      dfs(child, graph)
    stack.append(node)

  def find_topological_order(graph):
    all_nodes = set(graph.keys())
    while len(visited) < len(graph):
      print('visited nodes: %s' % visited)
      unvisited_nodes = all_nodes.difference(visited)
      dfs(next(iter(unvisited_nodes)), graph)

  find_topological_order(graph)

  ans = ''
  for i in range(len(stack)-1, 0-1, -1):
    ans += stack[i]

  return ans





