class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashing = set(nums)
        result = 0

        for i in nums:
            if i - 1 not in hashing:
                length = 1
                while i + 1 in hashing:
                    length += 1
                    i += 1
                result = max(result, length)
        return result