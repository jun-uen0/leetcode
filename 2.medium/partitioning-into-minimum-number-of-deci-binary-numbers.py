class Solution:
  def minPartitions(self, n: str) -> int:
    if len(n) == 1:
      return int(n)
    
    ans = 0
    for i in n:
      if ans == 9:
        return 9
      if int(i) > ans:
        ans = int(i)
    return ans