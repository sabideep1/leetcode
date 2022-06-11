from typing import List
class Solution():
    def firstIndex(self, nums,target):
        s = 0
        e = len(nums) - 1
        while s <= e:
            m = s+(e-s)//2
            if nums[m] == target:
               if (m-1 >=0 and nums[m-1] != target or m==0):
                   return m
               e = m - 1
            elif nums[m] > target:
                e = m -1
            else:
                s = m + 1
        return -1
    def lastIndex(self, nums, target):
        s1 = 0
        e1 = len(nums)  - 1
        while s1 <= e1:
            m1 = s1+(e1-s1)//2
            if nums[m1] ==target:
                if m1+1 <= e1 and nums[m1+1] != target or  m1 == len(nums)-1:
                    return m1
                s1 = m1+1
            elif nums[m1] >target:
                e1 = m1 -1
            else:
                s1 = m1+1

        return -1
    def searchRange(self, nums: List[int], target: int):
        left = self.firstIndex(nums,target)
        last = self.lastIndex(nums,target)

        return [left,last]


s = Solution()
s.searchSolution([1,2,3,4,5,6,6,6,7,7,7,8],6)
print(s)

                



    

