###############################################################################
# https://leetcode.com/problems/divide-two-integers/

# Given two integers dividend and divisor,
# divide two integers without using multiplication (x),
# division (÷f), and mod operator (%).

# The integer division should truncate toward zero,
# which means losing its fractional part.
# For example, 8.345 would be truncated to 8,
# and -2.7335 would be truncated to -2.

# Return the quotient after dividing dividend by divisor.
# quotient = the result of dividing two numbers

# Note: Assume we are dealing with an environment
# that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1].
# For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1,
# and if the quotient is strictly less than -2^31, then return -2^31.

# dividend: int
# divisor:  int
# output:   int

# divisor != 0 (dividend is possibility 0)
# -2^31 <= dividend, divisor <= 2^31 - 1

dividend = 10
divisor = -10

###############################################################################
# My solution
# Runtime: O(N)
# Status: Time Limit Exceeded

def divide() -> int:

  if (dividend == 0) or (divisor == 0):
    return 0
  
  dividend_abs = abs(dividend)
  divisor_abs = abs(divisor)
  
  count = 0
  while dividend_abs >= divisor_abs:
    count = count + 1
    dividend_abs -= divisor_abs

  if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
    return  -count
  else:
    return count

print(divide())

###############################################################################
# Other's solution (Faster time complexity)
def divide_faster() -> int: 
  if dividend == 0:
    return 0
  
  dividend_abs = abs(dividend)
  divisor_abs = abs(divisor)
  
  output = 0
  while dividend_abs >= divisor_abs:
    output = output + 1
    dividend_abs -= divisor_abs

  if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
    return  -output
  return output

print(divide_faster())









