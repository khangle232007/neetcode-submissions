class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1: return 0

        left, right = 0, 1
        result = 0 
        while right <= len(prices) - 1:
            if prices[right] >= prices[left]:
                profit = prices[right] - prices[left]
                result = max(result, profit)
                right += 1
            else:
                left = right
                right += 1
        return result