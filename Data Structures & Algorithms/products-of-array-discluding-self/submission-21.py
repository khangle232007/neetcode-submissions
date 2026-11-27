class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        prefix = 1
        for i in nums:
            result.append(prefix)
            prefix *= i
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result
        