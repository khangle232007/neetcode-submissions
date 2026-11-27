class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        left, right = 0, len(heights) - 1
        while left < right:
            if heights[left] > heights[right]:
                water = heights[right] * (right - left)
                right -= 1
            else:
                water = heights[left] * (right - left)
                left += 1
            result = max(result, water)
        return result
            