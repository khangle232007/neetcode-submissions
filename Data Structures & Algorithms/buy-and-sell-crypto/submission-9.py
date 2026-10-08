class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0 
        left = 0 
        right = 1
        while right <= len(prices) - 1:
            if prices[left] >= prices[right]:
                left = right
                right = left + 1
            elif prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                if profit > result:
                    result = profit
                if right == len(prices) - 1:
                    break 
                elif right < len(prices) - 1:
                    right += 1
        return result