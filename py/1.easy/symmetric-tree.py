# https://leetcode.com/problems/symmetric-tree/solutions

## Problem
# Given the root of a binary tree,
# check whether it is a mirror of itself
# (i.e., symmetric around its center).

## Examples
# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true
# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false

root = [1,2,2,3,4,4,3]

class Solution:
  def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    st = []
    if root:
      st.append([root.left, root.right])

    while(len(st) > 0):
      l, r = st.pop()

      if l and r:
        if l.val != r.val:
          return False
        st.append([l.left, r.right])
        st.append([r.left, l.right])

      elif l or r:
        return False

    return True