# https://leetcode.com/problems/find-k-pairs-with-smallest-sums

# Problem:
# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
# Define a pair (u,v) which consists of one element from the first array and one element from the second array.
# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.


# Example 1:
# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence:
#              [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

# Example 2:
# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [1,1],[1,1]
# Explanation: The first 2 pairs are returned from the sequence:
#              [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

# Example 3:
# Input: nums1 = [1,2], nums2 = [3], k = 3
# Output: [1,3],[2,3]
# Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]


# Constraints:
# 1 <= nums1.length, nums2.length <= 10^4
# -10^9 <= nums1[i], nums2[i] <= 10^9
# nums1 and nums2 both are sorted in ascending order.
# 1 <= k <= 1000

# Note:
# Duplicates OK
# 1st index is from nums1
# 2nd index is from nums2
# The 1st index must be [nums1[0],nums2[0]]
# The 2nd index must be []
# If the sum is same value, the order doesn't matter

# Input: nums1 = [1,2,3,4,5,6], nums2 = [1,100,101,102,103], k = 3
# Output: [1,1],[1,2],[1,3]
# Diff from nums[1]
# nums1 = [0,1,2,3,4,5] nums2 = [0,99,100,101,102]

# My Solution:
# Make an array in a loop
# The number of loop is k
# Compare sum(nums1[0] and nums2[1]) and sum(nums1[1] and nums2[0])
#         if sum(nums1[0] and nums2[1]) is smaller make and append array [nums1[0],nums2[1]]
#            and then campare sum(nums1[0],nums2[2]) and sum(nums1[1] and nums2[0])
#         el sum(nums1[1] and nums2[0]) is smaller make and append array [nums1[1],nums2[0]]
#            and then campare sum(nums1[1],nums2[1]) and sum(nums1[1] and nums2[0])

nums1 = [1,2,3,4,5,6]
nums2 = [1,2,3]
k = 3

def test(nums1,nums2,k):

  ans = [[nums1[0],nums2[0]]]

  # Base Case
  if k == 1:
    return ans

  idx1 = 0
  idx2 = 0

  for i in range(1,k):
    if nums1[0] + nums2[1] == nums1[1] + nums2[0]:
      ans.append([nums1[0],nums2[1]])
      ans.append([nums1[1],nums2[0]])
      idx1+=1
      idx2+=1
    elif nums1[0] + nums2[1] < nums1[1] + nums2[0]:
      ans.append([nums1[0],nums2[1]])
      # then campare sum(nums1[0],nums2[2]) and sum(nums1[1] and nums2[0])
      # if nums1[0] + nums2[2] > nums1[1] + nums2[0]
      # append [nums1[1] + nums2[0]]
      # then campare sum(nums1[0],nums2[2]) and sum(nums1[1] and nums2[1])

    else: # nums1[0] + nums2[1] > nums1[1] + nums2[0]:
      ans.append([nums1[1],nums2[0]])
      # then campare sum(nums1[0],nums2[1]) and sum(nums1[1] and nums2[1])



test(nums1,nums2,k)
