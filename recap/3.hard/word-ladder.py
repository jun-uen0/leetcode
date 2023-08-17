# https://leetcode.com/problems/word-ladder

# Problem
# A transformation sequence from word beginWord to word endWord using a dictionary wordList
# is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList,
# return the number of words in the shortest transformation sequence from
# beginWord to endWord, or 0 if no such sequence exists.

# Example 1:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5 
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
# Example 2:
# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

# Constraints:
# 1 <= beginWord.length <= 10
# endWord.length == beginWord.length
# 1 <= wordList.length <= 5000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.

# Notes:
# If endWord does not exist in wordList, return 0.
# And if beginWord == endWord, return 0, no need to transform.
# beginWord might not be in wordList.

# Solution:
# Ref: https://www.youtube.com/watch?v=h9iTnkgv05E
# We can use basic DFS to solve this problem.
# Time Complexity: O(nxm^2)
# 'hit' can be -> '*ot' or 'h*t' or 'ho*'
# 'dot' can be -> '*ot' or 'd*t' or 'do*'
# Oh hey, the 1st patterns of both words are the same
# {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hit'], 'ho*': ['hot']}
# 'dot' and 'lot' are neighbors of 'hot'

import collections


beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

def main():

  # Base case
  if endWord not in wordList:
    return 0

  # Make adjancecy list
  # Basically this is dictionary
  # But first time we insert value
  # The default value is empty list
  nei = collections.defaultdict(list)

  # wordList will be ['hot', 'dot', 'dog', 'lot', 'log', 'cog', 'hit']
  wordList.append(beginWord)

  # Update nei
  for word in wordList:
    for char in range(len(word)):
      pattern = word[:char] + "*" + word[char+1:]
      nei[pattern].append(word)

  # nei = {'*ot': ['hot', 'dot', 'lot'] ... '*it': ['hit'], 'hi*': ['hit']})

  visit = set([beginWord]) # {'hit'}
  q = collections.deque([beginWord]) # deque(['hit'])
  res = 1 # Check from next word, then next to next ... and so on

  # Loop while queue is not empty
  while q:

    # q: deque(['hit']]) -> deque(['hot', 'dot', 'lot']) ->
    #    deque(['dot', 'lot', 'dog']) -> deque(['lot', 'dog', 'log']) ->
    #    deque(['dog', 'log', 'cog']) -> deque(['log', 'cog']) -> deque(['cog'])
    # visit: {'hit'} -> {'hit', 'hot'} ... -> {'log', 'hit', 'cog', 'dog', 'hot', 'lot', 'dot'}
    
    for _ in range(len(q)):

      # Define word we will check
      word = q.popleft() # word: hit -> hot... -> cog

      # We found it!
      if word == endWord:
        return res
      
      for char in range(len(word)):

        # Define pattern for every each word, each word has 3 patterns
        pattern = word[:char] + "*" + word[char+1:]
        # pattern = '*it' -> 'h*t' -> 'hi*' ... lo*

        for neiWord in nei[pattern]:
          if neiWord not in visit:
            visit.add(neiWord)
            q.append(neiWord)
    
    res+=1 # Add how many neighbors we checked
  return 0

main()