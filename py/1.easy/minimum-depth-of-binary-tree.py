# https://leetcode.com/problems/minimum-depth-of-binary-tree/

## Problem
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path
# from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

## Examples
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

class Solution(object):
  def minDepth(self, root):
    if root is None:
      return 0
    if root.left is None and root.right is None:
      return 1

    l = self.minDepth(root.left)
    r = self.minDepth(root.right)
    
    if root.left is None:
      return 1 + r
    if root.right is None:
      return 1 + l
    
    return min(l, r) + 1