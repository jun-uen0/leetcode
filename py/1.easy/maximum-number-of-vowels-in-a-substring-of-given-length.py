# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length

# Problem:
# Given a string s and an integer k,
# return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Constraints:
# 1 <= s.le## 58. Length of Last Word

## My answer
# ```py
# class Solution:
#   def lengthOfLastWord(self, s: str) -> int:
#     return len(s.split()[-1])
# ```ngth <= 105
# s consists of lowercase English letters.
# 1 <= k <= s.length

# Solutoin:
# 1. for i in range(len(s))

# Test1:
# for i in range(len(s)):
#   print(i)
#   print(s[i]) 
# Output: 0 a 1 b 2 c 3 i 4 i 5 i 6 d 7 e 8 f
# Looped 8 times, but we need to loop only 7 times

# Test2:
# for i in range(len(s)-2):
#   print(s[i:i+k])
# Output: abc bci cii iii iid ide def

# My Solution:
# We need to check how many vowel letters is contained in each output(str)
# To do that, we need to create one more fucntion
# Let's say 'cnt_vowels'
# 'cnt_vowels' has one argument, str
# And we need to set a variable(number) outside of the 'cnt_vowels'
# Let's say 'cnt'
# If the counted number is greater than 'cnt' in the 'cnt_vowels', update the cnt
# Initial number of 'cnt" is 0
# If 'cnt' reaches to 'k', we don't need to update 'cnt' whild running 'cnt_vowels'
#    Becouse 'cnt' must be less than or equel to 'k'
# Note: if we handle same character for each iterative funtion, it will be more faster

# def cnt_vowles(str):
#   global cnt # To use cnt globally
#   # if cnt == k: return cnt # Base case (note: don't need in this function)
#   for i in range(k):
#     if any(str[i] in s for s in vwl):
#       cnt += 1
#   return
# cnt_vowles('abc')
# print(cnt) # Should be 1

# s = "rhythms"
# k = 4
# vwl = ['a','e','i','o','u']
# cnt = cnt_itr = 0
# for i in range(len(s)-k+1):
#   # if cnt == k: return cnt
#   pkt = s[i:i+k]
#   for j in range(k):
#     if any(pkt[j] in s for s in vwl):
#       cnt_itr += 1
#   # if cnt_itr > cnt:
#   #   cnt = cnt_itr
#   cnt = max(cnt_itr,cnt)
# print('cnt')
# print(cnt)
# Time Limit Exceeded: Too slow
# Time complexity is O(n x k)

# Other's Solution:
# Time complexity is O(n)
# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/discuss/648559/JavaPython-3-Slide-Window-O(n)-codes.

s = "abciiidef"
# 「abc」「bci」「cii」「iii」「iid」「ide」「def」
k = 3

# Make a dictionary contains all vowel
vowels = {'a', 'e', 'i', 'o', 'u'}

# Substitute 0 to ans and cnt
ans = cnt = 0

# For loop string s,
# i -> index of s
# v -> value of s
for i, v in enumerate(s):
  print('--')
  print('i is ',i)
  print('v is ',v)
  print('k is ',k)

  # If value is a vowel
  # Add 1 to cnt
  if v in vowels:
    print('if v in vowels')
    cnt += 1
    print('cnt is ',cnt)
  
  # When loop reach to number of k,
  # Even if find vowel, it's too much couting
  # So substract 1 from cnt
  if i >= k and s[i-k] in vowels:
    print('if i >= k and s[i-k] in vowels')
    print('s[i-k] is ',s[i-k])
    cnt -= 1
    print('cnt is ',cnt)
  
  # Get max number from cnt, ans
  # cnt can be nagative number
  ans = max(cnt, ans)
  print('ans is ',ans)
  print('cnt is ',cnt)

# print(ans)