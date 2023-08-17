# https://leetcode.com/problems/single-number-ii/description/

# Problem
# Given an integer array nums where every element appears three times except for one,
# which appears exactly once.
# Find the single element and return it.
# You must implement a solution with a linear runtime complexity
# and use only constant extra space.

# Examples
# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:
# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

nums_a = [2,2,3,2]
# nums_a = [0,1,0,1,0,1,99]
# nums_a = [0]

def singleNumber(nums):
  if len(nums) == 1:
    return nums[0]

  tmp1 = set()
  tmp2 = set()
  for n in nums:
    if n in tmp1:
      tmp2.add(n)
    else:
      tmp1.add(n)
  diff = tmp1 - tmp2
  return diff.pop()

print(singleNumber(nums_a))
