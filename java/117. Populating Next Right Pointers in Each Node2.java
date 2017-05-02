117. Populating Next Right Pointers in Each Node II

Follow up for problem Populating Next Right Pointers in Each Node.

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
"""
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""

/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */

public class Solution {
    public void connect(TreeLinkNode root) {
        TreeLinkNode tail = new TreeLinkNode(0);
        TreeLinkNode dummy = tail;
        TreeLinkNode node = root;

        while (node != null) {
          tail.next = node.left;
          if (tail.next != null) {
            tail = tail.next;
          }
          tail.next = node.right;
          if (tail.next != null) {
            tail = tail.next;
          }
          node = node.next;
          if (node == null) {
            tail = dummy;
            node = dummy.next;
          }
        }
    }
}