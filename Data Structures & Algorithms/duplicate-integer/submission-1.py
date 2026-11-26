class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashing = set()
        for i in range(len(nums)):
            if nums[i] in hashing:
                return True
            hashing.add(nums[i])
        return False