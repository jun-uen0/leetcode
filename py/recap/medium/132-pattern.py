## About
# URL: https://leetcode.com/problems/132-pattern
# Difficulty: Medium
# Topics: Stack


## Description
# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
# such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.

### 訳：
# n個の整数の配列numsが与えられる。
# 132パターンとは、nums[i], nums[j], nums[k]の3つの整数の部分列で、
# i < j < k かつ nums[i] < nums[k] < nums[j] となるものである。

# numsに132パターンがあればtrueを返し、なければfalseを返せ。

# sequence... 順序付けられたものの集まり


## Examples

# Example 1:
# Input: nums = [1,2,3,4]
# Output: false
# Explanation: There is no 132 pattern in the sequence.

# Example 2:
# Input: nums = [3,1,4,2]
# Output: true
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

# Example 3:
# Input: nums = [-1,3,2,0]
# Output: true
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


## Constraints
# n == nums.length
# 1 <= n <= 2 * 105
# -109 <= nums[i] <= 109

## Solution Note
# ※　We can return the anwsers immediately if we find the 132 pattern.
# numsでループを行う
# 最初の要素iを抽出、これは各ループ内で固定
# 二番目の要素jを抽出、これは残りの要素でループを行う必要がある


## Jeffrey's Methodology
# Find left,mid,right
# mid is should be as larger as possible
# left is should be as smaller as possible
# Iterate the list in reversed order
# Make a stack to store the temperory right value
# If current value is larger than top value (stack[-1]), then there is 32 pattern

def find132pattern_jef(nums):
  if len(nums) < 3:
    return False
  right = float('-inf') # -inf... ?
  stack = []
  for i in range(len(nums)-1, -1, -1): # (3, -1, -1)
    if nums[i] < right:
      return True
    else:
      while stack and stack[-1] < nums[i]:
        right = stack.pop()
    stack.append(nums[i])
  return False


# range() has three arguments
# for i in range(4,-1,-1):
#   print(i, end="")
# print() # 43210

## NeetCode's Solution
nums = [1,2,0,3,-1,6,3]
def find132pattern(nums):
  st = []
  curMin = nums[0]
  for n in nums[1:]:
    while st and n >= st[-1][0]:
      st.pop()
    if st and n > st[-1][1]:
      return True
    st.append([n,curMin])
    curMin = min(curMin,n)
  return False