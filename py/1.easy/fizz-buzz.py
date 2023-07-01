# https://leetcode.com/problems/fizz-buzz

def fizzBuzz(n):
  ans = []
  for v in range(1,n+1):
    if v % 15 == 0:
      ans.append("FizzBuzz")
    elif v % 3 == 0:
      ans.append("Fizz")
    elif v % 5 == 0:
      ans.append("Buzz")
    else:
      ans.append(str(v))
    
  return ans