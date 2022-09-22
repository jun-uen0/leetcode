# https://leetcode.com/problems/binary-search/
# GitHub copilot: Disable

# Problem:
# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums. If target exists,
# then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

# My solution:
# 1. Define the pivot number by dividing the nums array (floor)
# 2. Compare pivot number and target number.
# 3. If pivot number and target number both the same, return the pivot number
# 4. If pivot number is less than taget number, remove left of array from the search
# 5. If pivot number is greater than taget number, remove righ of array from the search
# 6. Try again from 1

# Input
# [5]
# 5
# Output
# 5
# Expected
# 0

nums = [-1,0,3,5,9,12]
target = 9
i = 0

def binary_search(nums,target):
  global i
  arr = nums
  m = (len(arr)-1)//2

  if len(arr) == 0:
    return -1
  elif arr[m] == target:
    return m + i
  elif arr[m] > target:
    arr = arr[:m]
    return binary_search(arr,target)
  elif arr[m] < target:
    i += m+1
    arr = arr[m+1:]
    return binary_search(arr,target)
  else:
    return 'error'

print(binary_search(nums,target))

# --- my answer ---------------------
i = 0
class Solution(object):
  def search(self, nums, target):
    global i
    arr = nums
    m = (len(arr)-1)//2

    if len(arr) == 0:
      return -1
    elif arr[m] == target:
      return m + i
    elif arr[m] > target:
      arr = arr[:m]
      return self.search(arr,target)
    elif arr[m] < target:
      i += m+1
      arr = arr[m+1:]
      return self.search(arr,target)
    else:
      return 'error'
