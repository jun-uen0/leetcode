# https://leetcode.com/problems/valid-sudoku

# Problem:
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
#              Since there are two 8's in the top left 3x3 sub-box, it is invalid.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# My solution:
# 1. For every row, Make a list and check if any value is duplicated, or not (every value except '.'): boolean
# 2. For every column, Make a list and check if any value is duplicated, or not (every value except '.'): boolean
# 3. For every subbox, Make a list and check if any value is duplicated, or not (every value except '.'): boolean
# If false, return falase
# Else if return true

board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["5",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

# 1. For every row, Make a list and check if any value is duplicated, or not (every value except '.'): boolean
def isContainSameNumInEveryCol(board): 
  for i in range(len(board)):
    temp = []
    for _,v in enumerate(board):
      if v[i] != '.':
        temp.append(v[i])
    if len(set(temp)) != len(temp):
      return True
  return False

print(isContainSameNumInEveryCol(board))

# 2. For every column, Make a list and check if any value is duplicated, or not (every value except '.'): boolean
def isContainSameNumInEveryRow(board):
  for i in range(len(board)):
    temp = [j for j in board[i] if j != '.']  
    if len(set(temp)) != len(temp):
      return True
  return False

print(isContainSameNumInEveryRow(board))

# 3. For every subbox, Make a list and check if any value is duplicated, or not (every value except '.'): boolean
def isContainSameNumInEverySubBox(board):
  l = 3
  for i in range(l):
    for j in range(l):
      temp = []
      for k in range(l):
        temp += board[3*i+k][3*j:l*(j+1)]
      temp = [m for m in temp if m != '.']
      if len(set(temp)) != len(temp):
        return True
  return False

print(isContainSameNumInEverySubBox(board))

def output(board):
  if (isContainSameNumInEveryCol(board)
    or isContainSameNumInEveryRow(board)
    or isContainSameNumInEverySubBox(board)):
    return False
  return True

print(output(board))