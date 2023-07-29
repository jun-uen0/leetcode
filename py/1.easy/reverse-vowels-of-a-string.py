# https://leetcode.com/problems/reverse-vowels-of-a-string/

## Problem
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u',
# and they can appear in both lower and upper cases, more than once.

## Examples
# Example 1:
# Input: s = "hello"
# Output: "holle"
# Example 2:
# Input: s = "leetcode"
# Output: "leotcede"

## Constraints:
# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.

s = "hello"
s = "leetcode"
vowels = ['a','e','i','o','u','A','E','I','O','U']

## Option one
# 1. store every vowels detected in 's' into dict (index num as key, the vowel as val)
#    "hello" -> {1:e, 4:o}
#    "leetcode" -> {1:e, 2:e, 5:,o, 7:e}
# 2. Somehow reverse the val
#    {1:e, 4:o} -> {1:o, 4:e}
#    {1:e, 2:e, 5:,o, 7:e} -> {1:e, 2:o, 5:,e, 7:e}
# 3. Replase the vowels
#    "hello" -> "holle"
#    "leetcode" -> "leotcede"

## Option two
# 1. Detect vowels in 's' in for loop starting from 0, and store in a list
# 2. Detect vowels in 's' in for loop starting from last idx, and replace from the list

# I go with option two
def reverseVowels(s):
  t = []
  cnt = 0
  a = []
  for v in reversed(s):
    if v in vowels:
      t.append(v)
  for v in s:
    if v in vowels:
      a.append(t[cnt])
      cnt+=1
    else:
      a.append(v)
  return ''.join(a)

print(reverseVowels(s))

# This is much more faster (https://leetcode.com/problems/reverse-vowels-of-a-string/solutions/1164745/python-solution-99-58-faster-86-96-less-memory/)
def reverseVowels_faster(s):
  s = list(s)
  left = 0
  right = len(s) - 1
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  while left < right:
    if s[left] in vowels and s[right] in vowels:
      s[left], s[right] = s[right], s[left]
      left += 1; right -= 1
    elif s[left] not in vowels:
      left += 1
    elif s[right] not in vowels:
      right -= 1

  return ''.join(s)