# https://leetcode.com/problems/implement-strstr/
# 'needle in a haystack' = very hard to find

# Given two strings needle and haystack,
# return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# For the purpose of this problem, we will return 0 when needle is an empty string. 

# haystack: str
# needle: str
# output: int

# For example,
# Given haystack = "hello", needle = "ll"
# Return 2.

###############################################################################
# My solution:

# haystack = "hello"
# needle = "ll"

# def split(word):
# 	return [char for char in word]

# haystack_lst = split(haystack)
# needle_lst = split(needle)

# print(haystack_lst)
# print(needle_lst)

# def needle_in_haystack() -> int:
#   st = []

#   for i in range(len(haystack_lst)):
#     if len(needle_lst) == 0:
#       if len(st) == 0:
#         return -1
#       else:
#         return len(st)
#     else:
#       st.append(haystack_lst[i])
#       if st[-1] == needle_lst[0]:
#         needle_lst.pop(0)
#       else:
#         st.pop(-1)
#   if len(st) == 0:
#     return -1
#   else:
#     return len(st)

# print(needle_in_haystack())

###############################################################################
# Other's solution (The best solution I've ever seen):
# class Solution:
def strStr(haystack: str, needle: str) -> int:
  
  if needle == "":
    return 0
  
  for i in range(len(haystack) + (len(needle)) -1):
    if haystack[i: i + len(needle)] == needle:
      return i
  
  return -1

  # (※) You don't need to convert the haystack and needle to lists.

  # Here is the explanation of the code:
  # 1. If needle is empty, return 0.
  # 2. If needle is not empty,
  #    2.1. Loop through the haystack
  #         For example, if haystack is "hello", and needle is "ll",
  #         range(len(haystack) -1 +(len(needle))) is going to be 6.
  #    2.2. If the haystack[i: i + len(needle)] == needle, return i
  #         For the first loop, haystack[0: 0 + len(needle)] is "he".
  #         For the second loop, haystack[1: 1 + len(needle)] is "el".