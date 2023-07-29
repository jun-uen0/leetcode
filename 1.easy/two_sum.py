# 2. Add Two Numbers
# https://leetcode.com/problems/two-sum

# Numbers in nums are not unique
# Numbers in nums are not sorted
# Only one valid answer exists
# There is an algorithm that is less than O(n2) time complexity

# nums = [3,2,3] # target = 6 # output = [0,2]
# nums = [-1,-2,-3,-4,-5] # target = -8 # output = [2,4]
# Length: len(nums)

def twoSum(nums, target):
  for i in range(len(nums)):
    for j in range(i+1,len(nums)):
      if nums[i] + nums[j] == target:
        return [i,j]
  return None