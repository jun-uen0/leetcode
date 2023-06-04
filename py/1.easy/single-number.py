# https://leetcode.com/problems/single-number/

## Problem
# Given a non-empty array of integers nums
# every element appears twice except for one
# find that single one
# complexity: linear runtime
    
## Examples
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:
# Input: nums = [1]
# Output: 1

# nums_a = [1,2,3,3,2]
nums_a = [1]

def singleNumber(nums):
  if len(nums) == 1:
    return nums[0]

  tmp = set()
  for n in nums:
    if n in tmp:
      tmp.remove(n)
    else:
      tmp.add(n)
  return tmp.pop()

print(singleNumber(nums_a))
