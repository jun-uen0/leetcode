# https://leetcode.com/problems/binary-tree-inorder-traversal

# Given the root of a binary tree,
# return the inorder traversal of its nodes' values.
# Traversal: left -> root -> right

# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Fastest Runtime: O(N)
# Worst Runtime: O(N)

# Solution:
# Use Depth first search to traverse the tree

from typing import List

class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    def dfs(root):
      if root is None: return
      dfs(root.left)
      res.append(root.val)
      dfs(root.right)
      return res
    return dfs(root)

###############################################################################
# Other's Solution:
# Time complexity: O(N)
# Iterative solution
# Link: https://zhenyu0519.github.io/2020/03/10/lc94/#methodology