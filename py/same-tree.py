# https://leetcode.com/problems/same-tree

# Given the roots of two binary trees p and q,
# write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, 
# and the nodes have the same value.

# Example1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Constraints:
# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104
# TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}

# Solutoin:
# Convert TreeNode to List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    
    p_lst = []
    q_lst = []
    def dfs(root, lst) -> List:
      if root is None: return
      if (root.left is None) or (root.right is None):
        lst.append('null')
      dfs(root.left,lst)
      lst.append(root.val)
      dfs(root.right,lst)
      return lst
    
    dfs(p,p_lst)
    dfs(q,q_lst)
    def is_same(lst1,lst2) -> bool:
      if len(lst1) != len(lst2):
        return False
      for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
          return False
      return True

    return is_same(p_lst,q_lst)
