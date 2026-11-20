import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right 
        while left <= right:
            middle = (left + right) // 2
            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / middle)
            if hours > h:
                left = middle + 1
            else:
                result = middle
                right = middle - 1
        return result