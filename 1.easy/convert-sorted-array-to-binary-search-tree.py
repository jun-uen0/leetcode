# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
# Very basic height balanced binary tree problem
# Good to recap the concept of height balanced binary tree

class Solution:
  def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
    if not nums:
      return None
    
    mid = len(nums)//2
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])

    return root