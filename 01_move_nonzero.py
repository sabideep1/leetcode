from typing import List
class Solution():
  def moveNonZero(self,arr: List[int]):
    j = 0
    for num in arr:
      if num != 0:
        arr[j] = num
        j += 1
    for num in range(j,len(arr)):
      arr[num] = 0

    return arr

s = Solution()
print(s.moveNonZero([1,0,0,0,0,2,0,3,0]))
