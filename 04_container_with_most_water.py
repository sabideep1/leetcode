from typing import List
class Solution():
    def maxWater(self,height: List[int]):
        left = 0
        right = len(height) - 1
        max_area = 0


        while left < right :
            area = (right - left) * (min(height[left],height[right]))
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area

s = Solution()
ans = s.maxWater([1,2,34,5,6,7,8])
print(ans)
