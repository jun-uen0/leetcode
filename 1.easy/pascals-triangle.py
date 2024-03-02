class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    # Base case
    if numRows == 1:
      return [[1]]

    ans = [[1],[1,1]]
    if numRows == 2:
      return ans

    # More than 2　rows
    for i in range(numRows-2):

      new_row = [1]
      for j in range(i+1):
        add = ans[i+1][j] + ans[i+1][j+1]
        new_row.append(add)

      new_row.append(1)
      ans.append(new_row)
    
    return ans