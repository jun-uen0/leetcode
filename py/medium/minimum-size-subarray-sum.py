# https://leetcode.com/problems/minimum-size-subarray-sum

# Problem:
# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr]
#   of which the sum is greater than or equal to target.
# If there is no such subarray, return 0 instead.

# Example 1:
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:
# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104

# Follow up:
# If you have figured out the O(n) solution,
# try coding another solution of which the time complexity is O(n log(n)).

# My Solution:
# 1. Loop nums
# 2. Make stack for each loop
# 3. Contain number of list to 'count' (initial: 0)

# [2]
# [2,3]
# [2,3,1]
# [2,3,1,2] # If greater than or equal to 7, return
# [2,3,1,2,4]
# [2,3,1,2,4,3]
#   [3,1]
#   [3,1,2]
#   [3,1,2,4]  # If greater than or equal to 7, return
#   [3,1,2,4,3]
#     [1,2]
#     ......

target = 7
nums = [2,3,1,2,4,3]

target = 11
nums = [1,1,1,1,1,1,1,1]

target = 11
nums = [1,2,3,4,5]
def minSubArr(nums,target):
  l = 0
  for i in range(len(nums)):
    st = []
    for j in range(len(nums) -i):
      st.append(nums[j+i])
      if sum(st) == target:
        if l > len(st) or l == 0:
          l = len(st)
  return l
# print(minSubArr(nums,target))

######################################
######################################
# WA: Should recap this
# Have to check if the value is not next
# Try out nums = [3,2,1,2,3], target = 4
# My code will output 0, but should be 2
######################################
######################################

# Second Solution:
# 1. Loop nums
# 2. Make stack for each loop
# 3. Contain number of list to 'count' (initial: 0)

# [2]
# [2,3]
# [2,3,1]
# [2,3,1,2]
# [2,3,1,2,4]
# [2,3,1,2,4,3]

# [2,  1]
# [2,  1,2]
# [2,  1,2,4]
# [2,  1,2,4,3]
# [2,    2]
# [2,    2,4]
# [2,    2,4,3]
# [2,      4]
# [2,      4,3]
# [2,        3]
# [2,3]
# [2,3,  2]
# [2,3,  2,4]
# [2,3,  2,4,3]
# [2,3,    4]
# [2,3,    4,3]
# [2,3,      3]
# [2,3,1]
# [2,3,1,  4]
# [2,3,1,  4,3]
# [2,3,1,2]
# [2,3,1,2,  3]
# [3]
# [3,1]
# [3,1,2]
# [3,1,2,3]
# [3,1,2,3,4]
# [3,1]
# ...

target = 7
nums = [2,3,1,2,4,3]

def minSubArrSec(nums,target):
  for i in range(len(nums)):
    st = []
    cnt = 0
    for j in range(len(nums)-i):
      if i == 0:
        st.append(nums[j])
        print(st)
      else:
        cnt += 1
      print(cnt)
        
  return None
print(minSubArrSec(nums,target))
  # l = 0
  # for i in range(len(nums)):
  #   st = []
  #   for j in range(len(nums) -i):
  #     st.append(nums[j+i])
  #     if sum(st) == target:
  #       if l > len(st) or l == 0:
  #         l = len(st)
  # return l