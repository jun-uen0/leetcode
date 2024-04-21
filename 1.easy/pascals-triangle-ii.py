# https://leetcode.com/problems/pascals-triangle-ii
# Fun to solve

# ① 1 -> 1 # Base case
# ② 11 -> zip (0,1) + (1,0)
#          (0,1): previous_row_start = [0] + row
#          (1,0): previous_row_start = row + [0]
#          -----
#          (1,1)
# ③ 121 -> zip (0,1,1) + (1,1,0)
#          (0,1,1): previous_row_start = [0] + row
#          (1,1,0): previous_row_start = row + [0]
#          -------
#          (1,2,1)
# ④ 1331 -> ...
# ⑤ 14641 -> ...

class Solution(object):
  def getRow(self, rowIndex):
    row = [1]

    for _ in range(rowIndex):
      previous_row_start = [0] + row
      previous_row_end = row + [0]
      new_row = []
      for x, y in zip(previous_row_start, previous_row_end):
        new_row.append(x + y)
      row = new_row
      
    return row