class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = []
        suffix = []
        for i in range(len(nums)):
            prefix.append(0)
            suffix.append(0)
        
        prefix[0] = 1
        suffix[-1] = 1
        
        #compute the prefix
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix[i - 1]

        #compute suffix
        for i in range(-2, -(len(nums) + 1), -1):
            suffix[i] = nums[i + 1] * suffix[i + 1]

        #calculate result
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        return result