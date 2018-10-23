298. Binary Tree Longest Consecutive Sequence

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

For example,
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
   2
    \
     3
    / 
   2    
  / 
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
-----------------------------------
Approach 1: Bottom up dfs - compute largest length containing current node, as you go up

Approach 2: Top down dfs - pass the length as you go down
-----------------------------------

class Node(object):
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


class Solution(object):
  def wrapper(self, node):
    self.best = 1
    self.dfs(node)
    return self.best
  def dfs(self, node):
    if not node: return 0
    temp = []
    cand = 1
    if node.left: 
      l = self.dfs(node.left) # returns the max chain using left child
      if node.left.val - 1 == node.val: temp.append(l)
    if node.right: 
      r = self.dfs(node.right) # returns the max chain using right child
      if node.right.val - 1 == node.val: temp.append(r)
    if temp: cand = max(temp) + 1
    self.best = max(self.best, cand)
    return cand


test1 = Node(3)
test1.left = Node(2)
test1.right = Node(4)
Solution().wrapper(test1)

head = Node(1)
head.right = Node(3)
head.right.left = Node(2)
head.right.right = Node(4)
head.right.right.right = Node(5)
Solution().wrapper(head)


# Top down
def dfs(node, parent, length):
  if not node: return length
  l = 1
  if parent and node.val == parent.val + 1:
    l = length + 1
  res = max(dfs(node.left, node, l), dfs(node.right, node, l))
  return max(res, l)

dfs(test1, None, 1)
dfs(head, None, 1)
