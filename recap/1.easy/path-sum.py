# https://leetcode.com/problems/path-sum/

# Given the root of a binary tree and an integer targetSum,
# return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

# Constraints:
# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# Note:
# The tree is binary and each node has a value stored in a property called val.
# TreeNode{val: 5, left: TreeNode{val: 4, left: TreeNode{val: 11, left: TreeNode{val: 7, left: None, right: None}, right: TreeNode{val: 2, left: None, right: None}}, right: None}, right: TreeNode{val: 8, left: TreeNode{val: 13, left: None, right: None}, right: TreeNode{val: 4, left: None, right: TreeNode{val: 1, left: None, right: None}}}}

# How to solve?:
# Can not use breadth-first search, because the tree is not a linear structure. So we need to use depth-first search.
# I think it's efficient to use recursive call.
# Basically return False, but if the tree has a path sum of targetSum, return True.
# The function is for the each node, and the recursive call is for the left and right subtree. 
# How to run O(logN) time?

from typing import Optional
class TreeNode:
  
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
      def dfs(node,cur_sum):
        if not node: # If the node is None (not exist), return False
          return False
        cur_sum += node.val # Add the value of the node to the current sum
        if not node.left and not node.right: # Check if the node has no children
          return cur_sum == targetSum # If the sum is equal to the targetSum, return Truec
        # Return the result of the left and right subtree
        return dfs(node.left,cur_sum) or dfs(node.right,cur_sum) # If the first return is True, return the first result. If the first return is False, return the second result.
      return dfs(root,0) # Start the dfs from the root, and initialize the current sum as 0