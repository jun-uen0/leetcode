# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Problem:
# Given a string s,
# find the length of the longest substring
# without repeating characters.

# Example 1:
# Input: s = "abcabcbb" -> "abc", "ab∂c"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1. 
# ※ Without repeating characters.

# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# ※ The difference between substring and subsequence is that substring is contiguous, subsequence is not.

# Example 4:
# Input: s = ""
# Output: 0

# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

# My Solution:
# Base Case: If s is empty, return 0
# Make loop for len(s)
# Contain each char in temp var
# And count
# Update most longest substring

def lengthOfLongestSubstring(s: str):
  # Base Case
  if len(s) == 0: return 0
  if len(s) == 1: return 1
  
  cnt = 0
  tmp = [s[0]]

  for i in range(1,len(s)):
    if s[i] in tmp:
      tmp = tmp[tmp.index(s[i])+1:]
    tmp.append(s[i])
    if len(tmp) > cnt:
      cnt = len(tmp)
  return cnt

print(lengthOfLongestSubstring(s))　