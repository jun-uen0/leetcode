# https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/description/

## Problem
# Given an array of integers arr.
# We want to select three indices i, j and k
# where (0 <= i < j <= k < arr.length).
# Let's define a and b as follows:
# a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
# b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
# Note that ^ denotes the bitwise-xor operation.
# Return the number of triplets (i, j and k) Where a == b.

## Examples
# Example 1:
# Input: arr = [2,3,1,6,7]
# Output: 4
# Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
# Example 2:
# Input: arr = [1,1,1,1,1]
# Output: 10

# a is XOR between i and j - 1
# b is XOR between j and k
# if a == b, count the triplet

arr = [2,3,1,6,7]
def countTriplets(arr):
  # ln = len(arr) -1
  # cnt = 0

  # for i in range(ln):
  #   for j in range(i+1,ln+1):
  #     for k in range(j,ln+1):
  #       a,b = 0,0
  #       for idx in range(i,j-1):
  #         if idx == i:
  #           a = arr[i]
  #           continue
  #         a ^= arr[idx]
  #       for idx in range(j,k):
  #         if idx == j:
  #           b = arr[j]
  #           continue
  #         b ^= arr[idx]

  #       if a == b:
  #         cnt+=1

  # return cnt

  n = len(arr)
  prefix = [0 for i in range(n)] # [0, 0, 0, 0, 0]

  ans = 0
  for i in range(n):
    prefix[i] = prefix[i-1] ^ arr[i] if i >= 1 else arr[i]
  
  cnt = 0
  for j in range(i-1):
    if prefix[i]==prefix[j]:
      cnt += i - j - 1
    if prefix[i] == 0:
      cnt += i
  ans += cnt

  return ans

print(countTriplets(arr))