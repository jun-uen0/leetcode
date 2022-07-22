# https://leetcode.com/problems/subarray-sum-equals-k/description

# Description:
# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# Constraints:
# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 10

# nums = [1, 1, 1]
# k = 2

# def subarray_sum(nums, k):

#   count = 0
#   for i in range(len(nums)):
#     if nums[i] == k:
#       count += 1
#     # You don't need to culc if the el is greater than k
#     # Only if the el is less than k, you have to continue
#     if nums[i] < k:
#       for j in range(1,len(nums) -i):
#         print('i')
#         print(i)
#         print('j')
#         print(j)
#         print('nums[i:i+j]')
#         print(nums[i:i+j])
#         if sum(nums[i:i+j]) == k:
#           count += 1
  
#   return count


# print(subarray_sum(nums,k))

###############################################################################
# Other's Solution:
# Time conprexity: O(N)
# Use hashmap to record all sum(0 to x) (as the key)
# nums = [2,2,3,0,2,-1,1,6,-3,3]
# k = 7

nums = [9,9,9]
k = 18
# output = 5
def subarraySum() -> int:
  cnt = 0
  total = 0
  cache = {0:1} # Why use 0 as the key? Because if the sum is 0, then there is one subarray with 0
  for v in nums: # v is the current element
    print('------------------------')
    total += v # adding the current element to the total
    print('(total += i) total = ', total)
    print('v in for', v)
    # if cache.get(total-k), count the subarray.
    # For example, if total = 7, then cache.get(7-k) = 1
    # For more examples, if total = 9, then cache.get(9-k) = 2
    if cache.get(total-k): # When total-k exists in the cache, then count the subarray
      print('cache.get(total-k) is called')
      print('total-k:', total-k)
      print('cache.get(total-k):', cache.get(total-k))
      print('v: ', v)
      cnt += cache[total-k]
      print('cnt: ', cnt)
      print('cache: ', cache)
    if cache.get(total): # When total exists in the cache, then add 1 to the count. Why? Because if the sum is 0, then there is one subarray with 0
      print('cache.get(total) is called')
      print('v: ', v)
      cache[total] += 1
      print('cache: ', cache)
    else:
      print('else is called')
      print('v: ', v)
      cache[total] = 1
      print('cache: ', cache)
  return cnt

print(subarraySum())