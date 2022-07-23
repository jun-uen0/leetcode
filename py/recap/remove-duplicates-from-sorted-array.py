# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# nums sorted in non-decreasing order
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Example 2:
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

from typing import List # Need this for the type annotation
nums = [1,1,1,2,2,3,3,4]
def remove_duplicates(nums: List[int]) -> int:
  d = 0
  for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
      d+=1
    else:
      nums[i-d] = nums[i]
  print(nums)
  return len(nums) - d
print(remove_duplicates(nums)) # 4