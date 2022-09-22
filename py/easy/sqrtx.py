# https://leetcode.com/problems/sqrtx

# Given a non-negative integer x,
# compute and return the square root of x.

# Since the return type is an integer,
# the decimal digits are truncated, 
# and only the integer part of the result is returned.

# Note: You are not allowed to use 
# any built-in exponent function or operator, 
# such as pow(x, 0.5) or x ** 0.5.

# Example 1:
# Input: x = 4
# Output: 2

# Example 2:
# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., 
#   and since the decimal part is truncated, 2 is returned.

# Constraints:
# 0 <= x <= 231 - 1e-9

# Other's Solution:
# Time Conprexity: O(LogN)
# Use binary search to find the square root
# https://leetcode.com/problems/sqrtx/discuss/25061/Python-binary-search-solution-(O(lgn))
def faster_sol(x):
  l, r = 0, x
  while l <= r:
    mid = l + (r-l)//2
    if mid * mid <= x < (mid+1)*(mid+1):
      return mid
    elif x < mid * mid:
      r = mid - 1
    else:
      l = mid + 1

###############################################################################

# My solution:
# From 1, to x, check if the square root is equal to the target number
# Time Conprexity: O(N)

x = 256
def mySqrt(x) -> int:
  if x == 0:
    return 0
  if x == 1:
    return 1
  if x == 2:
    return 1
  for i in range(1,x):
    if i*i > x:
      return i-1
    if i*i == x:
      return i

print(mySqrt(x)) # 	Accepted: But too slow

###############################################################################
# My solution 2:
# Multiple the number by 2 and check if the square root is equal to the target number
# Time conprexity: O(LogN)?
def my_sqrt_2(x) -> int:
  if x == 0: 
    return 0
  if x == 1 or x == 2: 
    return 1
  for i in range(2,x):
    if i*i > x: return i-1 # 2: 2,3
    if i*i == x: return i  # 2: 4
    while i*i < x: # 2: 5,6,7...
      mul = 1
      temp = 0 # 2, x=16, temp=4
      for v in range(1,mul):
        temp *= i
        print('temp is: ', temp)
      if temp*temp > x:
        # print('less than 16')
        break
      if temp*temp == x:
        return temp
      if temp*temp < x:
        # print('one more mul')
        mul += 1 # gonna be 2, 
        # and want to do i*i*i in next loop, not i*i*2
        break
print(my_sqrt_2(x)) # WA: Time Limit Exceeded