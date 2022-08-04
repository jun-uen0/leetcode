# https://leetcode.com/problems/length-of-last-word

# Problem:
# Given a string s consisting of words and spaces,
# return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.

# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.

# My solution:
# 1. Split the string by space
# 2. Add every splited word in a list
# 3. Reture the number of last word

s = "   fly me   to   the moon  "
# print(s.split()) # ['fly', 'me', 'to', 'the', 'moon']
print(len(s.split()[-1]))
