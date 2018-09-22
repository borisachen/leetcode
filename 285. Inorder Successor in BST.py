285. Inorder Successor in BST

Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

Note: If the given node has no in-order successor in the tree, return null.

------------------------------------
1. We can do a full in order traversal, store the element in order in a list.
then travese the list and return the element after the target.
O(n) where n is the number of nodes

2. Supposedly there is an O(h) solution?
In a BST we can locate the target node with binary search in O(h)
Once we find the target, what do we do to find the successor?

case 1 - if the target node has a right subtree, then the successor must be in the right subtree.
  boils down to finding the smallest element in the right subtree.
  this can be done by going left as far as possible.
case 2 - if target node has NULL full right child, then what?
  then it is somewhere above it. how do we find it?
  travel down the tree. 
  if target < root.val, then 
    set successor = root and 
    move root to root.left.
  else if target > root.val, then set root to root.right.
  else, we target==root.val so we found the target.
  Why does this work?
  we are looking for the next largest node that is bigger than target.
  if target is less the current root, then the current root could be the successor, so update successor pointer and search left
  if target is greater than current root, the current root then previous candidate could still be the successor.

------------------------------------

# first find the target node.
def find_target(root, target):

	


# case one:
