# https://leetcode.com/problems/sort-an-array/

## Problem
# Given an array of integers nums, sort the array in ascending order and return it.
# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity
# and with the smallest space complexity possible.

## Examples
# Example 1:
# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:
# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique

nums = [5,1,1,2,0,0]

def sortArray(nums):
  def merge_arrs(l, r , nums):
    print(f'merge_arrs is called')
    i, j, k = 0, 0, 0
    while i < len(l) and j < len(r):
      if l[i] < r[j]:
        nums[k] = l[i]
        i += 1
      else:
        nums[k] = r[j]
        j += 1
      k += 1
    
    nums[k:] = l[i:] if i < len(l) else r[j:]
    print(f'nums is',nums)
      
  def merge_sort(nums):
    if len(nums) == 1: return nums
    
    m = len(nums) // 2
    l, r = nums[:m], nums[m:]
    print(f'm is',m)
    print(f'l is',l)
    print(f'r is',r)
    print('---')
    
    merge_sort(l)
    merge_sort(r)
    
    merge_arrs(l, r, nums)
  
  merge_sort(nums)
  return nums

print(sortArray(nums))