from typing import List
class Solution():
  def mountainArray(self,arr: List[int]) -> bool:
    if len(arr) < 3:
        return False
    i = 1
    while (i < len(arr) and arr[i] > arr[i-1]):
        i += 1
    if ( i==1):
        return False
    while (i < len(arr) and arr[i] < arr[i-1]):
        i +=1
    return i == len(arr)
    

            

s = Solution()
answer = s.mountainArray([1,2,1008,700,30,2])
print(answer)

