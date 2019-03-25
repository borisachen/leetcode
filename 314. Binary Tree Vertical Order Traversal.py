314. Binary Tree Vertical Order Traversal
(locked)

Given a binary tree, return the vertical order traversal of its nodes values.
(ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to
right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]
                   0 1 2 3 4 5 6 7.   8.   9.   1011
Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
----------------------------------------------
Well we know there are vertical columns a head of time and the root is 0.
         root
-3 -2 -1  0  1  2  3
We could keep track of the x coordinate as we recurse through the tree.
Use a dictionary to store each node that we see
d: key = x coordinate, value = node value
when we recurse left, we pass the current coordinate - 1, right would be +1?
----------------------------------------------

def vertical_order(tree):
  res = {}
  dfs(0, 0, tree, res)
  min_key = min(res.keys())
  max_key = max(res.keys())
  ans = []
  for i in range(min_key, max_key+1):
    ans.append(res[i])
  return ans

def dfs(index, xcoord, tree, res):
  if index > len(tree) or tree[index] == None:
    return
  if xcoord in res:
    res[xcoord].append(tree[index])
  elif xcoord not in res:
    res[xcoord] = [tree[index]]
  left = index * 2 + 1
  right = index * 2 + 2
  if left < len(tree):
    dfs(left, xcoord-1, tree, res)
  if right < len(tree):
    dfs(right, xcoord+1, tree, res)

vertical_order([3,9,8,4,0,1,7])

vertical_order([3,9,8,4,0,1,7,None,None,None,2,5])
