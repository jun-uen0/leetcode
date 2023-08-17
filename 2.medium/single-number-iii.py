# https://leetcode.com/problems/single-number-iii

### Problem
# Given an integer array nums,
# in which exactly two elements appear only once
# and all the other elements appear exactly twice.
# Find the two elements that appear only once.
# You can return the answer in any order.
# You must write an algorithm
# that runs in linear runtime complexity
# and uses only constant extra space.

### Examples
## Example 1:
# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.
## Example 2:
# Input: nums = [-1,0]
# Output: [-1,0]
## Example 3:
# Input: nums = [0,1]
# Output: [1,0]

nums = [1,2,1,3,2,5] 

def singleNumber(nums):
  if len(nums) == 2:
   return nums

  tmp1 = set()
  tmp2 = set()

  for n in nums:
    if n in tmp1:
      tmp2.add(n)
  tmp1.add(n)

  diff = tmp1 - tmp2
  return list(diff)

print(singleNumber(nums))

#### Other's beatiful code #####
# def checkBit(n, i):
#   return (n & (1<<i))!=0

# def getSetBitPos(n):
#   for i in range(32):
#     if checkBit(n, i):
#       return i

# def singleNumber(nums) -> list[int]:
#   x, n = 0, len(nums)
#   # Basic case
#   if n == 2:
#     return nums
#   # Get XOR of all elements of nums
#   # And then plug the result into x
#   for i in range(n):
#     x ^= nums[i]
#   # Identify the position of the first '1' bit
#   # when counting from the least significant digit (rightmost)
#   pos = getSetBitPos(x)
#   x1,x2 = 0,0
#   for i in range(n):
#     if checkBit(nums[i],pos):
#       # 2,3,2
#       x1 ^= nums[i]
#     else:
#       # 1,1,5
#       x2 ^= nums[i]
#   return [x1, x2]