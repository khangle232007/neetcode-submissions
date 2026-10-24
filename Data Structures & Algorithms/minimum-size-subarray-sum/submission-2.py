class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        1/ put left and right at 0
        2/ while the sum in that window is < target:
            right += 1
            if the sum in that window is >= target:
                left += 1
            result = right - left + 1

            keep doing that loop
            if the current result is smaller than previous one, update 
            result
        """
        left = 0
        res = float('inf')
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            print(curr_sum)
            while curr_sum >= target:
                curr_sum -= nums[left]
                left += 1
                res = min(right - left + 2, res)
            
        return res if res != float('inf') else 0
                
        
            
            