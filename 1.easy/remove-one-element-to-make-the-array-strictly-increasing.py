# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing

# Problem:
# Given a 0-indexed integer array nums, return true
#   if it can be made strictly increasing after removing exactly one element,
#   or false otherwise. If the array is already strictly increasing, return true.
# The array nums is strictly increasing
#   if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

# Example 1:
# Input: nums = [1,2,10,5,7]
# Output: true
# Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
# [1,2,5,7] is strictly increasing, so return true.

# Example 2:
# Input: nums = [2,3,1,2]
# Output: false
# Explanation:
# [3,1,2] is the result of removing the element at index 0.
# [2,1,2] is the result of removing the element at index 1.
# [2,3,2] is the result of removing the element at index 2.
# [2,3,1] is the result of removing the element at index 3.
# No resulting array is strictly increasing, so return false.

# Example 3:
# Input: nums = [1,1,1]
# Output: false
# Explanation: The result of removing any element is [1,1].
# [1,1] is not strictly increasing, so return false.

# My Solution 1 O(N2) :
# Remove each element from nums: 0(N)
#   While we remove the element, check if the nums is strictly increasing
#   How to check that? Compare each element and next element: O(N)
#     If the element is greater than next one, return false

nums = [2,3,1,2]

def canBeIncreasing(nums):
  for i,v in enumerate(nums):
    nums.pop(i)
    res = all(i < j for i, j in zip(nums, nums[1:]))
    if res is True:
      return True
    nums.insert(i,v)
  return False

print(canBeIncreasing(nums))

# Reference for Check if list is strictly increasing
# https://www.geeksforgeeks.org/python-check-if-list-is-strictly-increasing/