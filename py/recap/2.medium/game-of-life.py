# https://leetcode.com/problems/game-of-life/

# Problem:
# According to Wikipedia's article:
# "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
#
# The board is made up of an m x n grid of cells,
# where each cell has an initial state: live (represented by a 1) or dead (represented by a 0).
# Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
# using the following four rules (taken from the above Wikipedia article):
#
# 1. Any live cell with fewer than two live neighbors dies as if caused by under-population.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by over-population.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
# The next state is created by applying the above rules simultaneously
# to every cell in the current state, where births and deaths occur simultaneously.
# Given the current state of the m x n grid board, return the next state.
#
# 訳：
# Wikipediaの記事によると、
# "ゲーム・オブ・ライフ（Game of Life）は、
# イギリスの数学者であるジョン・ホルトン・コンウェイが1970年に考案したセル・オートマトンである。"
#
# このボードは、m x nのグリッドのセルからなり、
# 各セルは初期状態で生きている（1で表される）か死んでいる（0で表される）かを持つ。
# 各セルは、水平、垂直、斜めの8つの近傍セルと相互作用し、
# 以下の4つのルール（Wikipediaの記事から引用）に従う。
#
# 1. 2つ未満の生きている近傍セルを持つ生きているセルは、
#    過疎によって死ぬ。
# 2. 2つまたは3つの生きている近傍セルを持つ生きているセルは、
#    次の世代に生き残る。
# 3. 3つより多くの生きている近傍セルを持つ生きているセルは、
#    過密によって死ぬ。
# 4. 死んでいるセルに3つの生きている近傍セルがある場合は、
#    再生によって生きているセルになる。
#
# 次の状態は、現在の状態のすべてのセルに対して、
# 同時に上記のルールを適用して作成される。
# つまり、誕生と死亡は同時に発生する。
# 現在のm x nグリッドボードの状態を返せ。

# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]

# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
board = [[0]]
board = [[0,0]]
def gameOfLife(board):

  if board == [[0]]:
    print([[0]])
  if board == [[1]]:
    print([[1]])

  # ans = [[0] * len(board[0])] * len(board) <- BAD!!
  ans = [[0] * len(board[0]) for _ in range(len(board))]
  nei_alive = 0

  for m in range(len(board)):
    for n in range(len(board[0])):

      # Top
      if m == 0:
        # Top Left
        if n == 0:
          nei_alive = [board[m][n+1],board[m+1][n],board[m+1][n+1]].count(1)
        # Top Right
        elif n == len(board[0])-1:
          nei_alive = [board[m][n-1],board[m+1][n-1],board[m+1][n]].count(1)
        # Top, not Left or Right
        else:
          nei_alive = [board[m][n-1],board[m][n+1],board[m+1][n-1],board[m+1][n],board[m+1][n+1]].count(1)

      # Bottom
      elif m == len(board)-1:
        # Bottom Left
        if n == 0:
          nei_alive = [board[m-1][n],board[m-1][n+1],board[m][n+1]].count(1)
        # Bottom Right
        elif n == len(board[0])-1:
          nei_alive = [board[m-1][n-1],board[m-1][n],board[m][n-1]].count(1)
        # Bottom, not Left or Right
        else:
          nei_alive = [board[m-1][n-1],board[m-1][n],board[m-1][n+1],board[m][n-1],board[m][n+1]].count(1)

      # Not top or bottom
      else:
        # Most left
        if n == 0:
          nei_alive = [board[m-1][n],board[m-1][n+1],board[m][n+1],board[m+1][n],board[m+1][n+1]].count(1)
        # Most right
        elif n == len(board[0])-1:
          nei_alive = [board[m-1][n-1],board[m-1][n],board[m][n-1],board[m+1][n-1],board[m+1][n]].count(1)
        # Not most left or right, not top or bottom
        else:
          nei_alive = [
            board[m-1][n-1],board[m-1][n],board[m-1][n+1],
            board[m][n-1],board[m][n+1],
            board[m+1][n-1],board[m+1][n],board[m+1][n+1]].count(1)

      if board[m][n] == 1:
        if nei_alive == 2 or nei_alive == 3:
          ans[m][n] = 1
      else:
        if nei_alive == 3:
          ans[m][n] = 1

  for i in range(len(board)):
    for j in range(len(board[0])):
      board[i][j] = ans[i][j]
  
  print(board)

# gameOfLife(board)

# print('---')
# test = [[0] * 3] * 3
# print(test)
# test[0][0] = 5
# print(test)

# print('---')
# test2 = [[0] * 3 for _ in range(3)]
# print(test2)
# test2[0][0] = 5
# print(test2)

# Other's Solution:

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
def gameOfLife(board):
  m,n = len(board), len(board[0])
  for i in range(m):
    for j in range(n):
      if board[i][j] == 0 or board[i][j] == 2:
        if nnb(board,i,j) == 3:
          board[i][j] = 2
        else:
          if nnb(board,i,j) < 2 or nnb(board,i,j) >3:
            board[i][j] = 3
  for i in range(m):
    for j in range(n):
      if board[i][j] == 2: board[i][j] = 1
      if board[i][j] == 3: board[i][j] = 0
  
            
def nnb(board, i, j):
  m,n = len(board), len(board[0])
  count = 0
  if i-1 >= 0 and j-1 >= 0:   count += board[i-1][j-1]%2
  if i-1 >= 0:                count += board[i-1][j]%2
  if i-1 >= 0 and j+1 < n:    count += board[i-1][j+1]%2
  if j-1 >= 0:                count += board[i][j-1]%2
  if j+1 < n:                 count += board[i][j+1]%2
  if i+1 < m and j-1 >= 0:    count += board[i+1][j-1]%2
  if i+1 < m:                 count += board[i+1][j]%2
  if i+1 < m and j+1 < n:     count += board[i+1][j+1]%2
  return count

print(gameOfLife(board))