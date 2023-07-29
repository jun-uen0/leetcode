# https://leetcode.com/problems/intersection-of-two-arrays-ii

## Problem
# Given two integer arrays nums1 and nums2,
# return an array of their intersection.
# Each element in the result must appear as many times as it shows
# in both arrays and you may return the result in any order.

## Example
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

nums1 = [1,2,2,1]
nums2 = [2,2]

def intersect(nums1,nums2):
  tmp1 = nums1
  tmp2 = nums2
  ans = []

  for i in range(len(tmp1)):
    if len(tmp2) == 0:
      return ans
    if tmp1[i] in tmp2:
      ans.append(tmp1[i])
      tmp2.remove(tmp1[i])
  return ans
print(intersect(nums1,nums2))