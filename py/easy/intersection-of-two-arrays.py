## About
# URL: https://leetcode.com/problems/intersection-of-two-arrays
# Difficulty: Easy
# Tags: array, hash-table, two-pointers, binary-search, sor


## Description
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.


## Examples
# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.


## Constraints
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


## My solution
# 1. Merge sort both arrays
# 2. Eliminate duplicates from both arrays
# 3. Iterate through shorter array and check if element is in longer array

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
def rm_d(lst):
  lst.sort()
  d = 0
  for i in range(1,len(lst)):
    if lst[i] == lst[i-1]:
      d+=1
    else:
      lst[i-d] = lst[i]
  return lst[0:len(lst)-d]

def bs(trgt,lst,r,l):
  while r <= l:
    m = (r+l)//2
    if lst[m] == trgt:
      return True
    elif lst[m] > trgt:
      l = m-1
      return bs(trgt,lst,r,l)
    else:
      r = m+1
      return bs(trgt,lst,r,l)
  return False
  

def intersection(nums1,nums2):

  # Merge sort both arrays
  # Eliminate duplicates from both arrays
  no_d_1 = rm_d(nums1)
  no_d_2 = rm_d(nums2)

  st = []

  # Iterate through shorter array and check if element is in longer array
  # If length of both is same, let's iterate nums1
  if len(no_d_1) <= len(no_d_2):
    for _,v in enumerate(no_d_1):

      # Binary search in no_d_2 with v
      # If found append v to st
      if bs(v,no_d_2,0,len(no_d_2)-1):
        st.append(v)

  else:
    for _,v in enumerate(no_d_2):
      if bs(v,no_d_1,0,len(no_d_1)-1):
        st.append(v)
  
  return st

# print(intersection(nums1,nums2))


## Other's Solution
# URL: https://donic0211.medium.com/leetcode-349-intersection-of-two-arrays-9f99b27cf247

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

def intersection(nums1, nums2):
  return list(set(nums1) & set(nums2))

# print(intersection(nums1,nums2))

set1= {2, 1, 2, 3, 2, 3, 1, 3, 3, 1}
set2= {2, 4, 5, 6, 7, 4, 4, 5, 6, 9, 7}
print(set1)
print(set2)
print(list(set1 & set2))




