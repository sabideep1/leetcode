from typing import List
class Solution():
    def boatsRequired(self,people: List[int],limit: int):
        people.sort()
        left = 0
        right = len(people) - 1
        boats_required = 0
        while left <= right:
            if left == right:
                boats_required += 1
                break
            if (people[left] + people[right] <= limit):
                left += 1
                right -= 1
            else:
                right -= 1

            boats_required += 1
            
            
        return boats_required

s = Solution()
print(s.boatsRequired([2,2,2,3,3],4))

