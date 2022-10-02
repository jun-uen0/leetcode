## About
# URL: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Difficulty: Medium
# Tags: Array, BinarySearch


## Description
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function,
# nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0],
# nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# 訳：
# 昇順にソートされた整数配列numsが与えられる。(重複なし)
# この配列は、不明なピボットインデックスk(1 <= k < nums.length)で回転される可能性がある。
# その結果、配列は[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]](0-indexed)になる。
# 例えば、[0,1,2,4,5,6,7]は、ピボットインデックス3で回転され、[4,5,6,7,0,1,2]になる。
# 回転後の配列numsと整数targetが与えられたとき、
# numsにtargetが含まれている場合はそのインデックスを、含まれていない場合は-1を返せ。
# O(log n)の実行時間で解く必要がある。


## Example
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1


## Constraints
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104


## My solution
# 1. Fix array
# 2. Execute Binary Search with target value

## Note
# How to fix array?
# Compare fist el and last el
# If last el is smaller than first el, relocate last el to first el
# For example, nums is [3,4,5,2] -> [2,3,4,5]
# And then, Compare fist el and last el
# If last el is greater than first el, array is fixed
# But this method is unefficient.
# We need to do this with O(LogN)
# Can we do this exponentially?
# For example, first time in loop, just compare nums[-1] and first value (as target)
# And then, for next loop, we compare nums[-2] and fist
# For 3rd loop, we skip to compare nums[-3], but nums[-4]
# For 4th loop, we skip to compare nums[-5],[-6] and [-7], but nums[-8] and so on.
# Let's say if nums is [15, ... 112,133,146,3,10,11,12,13,14]
# In 4th loop, we notice that nums[-8] is smaller than first value because nums[-8] is 133n
# Which means, real first value of array is in range of nums[-7] and nums[-5]
# For 5th loop, we campare nums[(-7 + (-5))//2 = -6] and first value
# nums[-6] is 3. It's smaller than last el. We did not find greater value yet.
# For 6th loop, we compare nums[-7] and first value
# nums [-6] is 146. We finally found real last value
# Real first value is in nums[-6] and real last value is in nums[-7]
# We relocate nums[:-6] to nums[6:]
# Then array must be fixed up 
# We can't use basic binary search in this loop

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    
    rotate = 0
    
    # Fix array
    if nums[0] > nums[-1]:
      l = 1
      r = len(nums) -1
      tmp = r
      while l <= r:
        mid = (l + r) // 2
        if nums[mid] > nums[0]:
          l = mid + 1
        else:
          r = mid - 1

      nums = nums[l:] + nums
      del nums[tmp+1:]
      rotate = l
    
    # Execute Binary Seach
    s = 0
    e = len(nums) - 1
    while s <= e:
      mid = (s + e) // 2
      print('mid is ', mid)
      if nums[mid] == target:
        if mid + rotate >= len(nums):
          return mid + rotate - len(nums)
        return mid + rotate
      if nums[mid] > target:
        e = mid - 1
      else:
        s = mid + 1
    return -1