class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        hashing = set(nums)
        for i in range(len(nums)):
            if (nums[i] - 1) not in hashing:
                current_number = nums[i]
                current_sequence = 1
                while (current_number + 1) in hashing:
                    current_number += 1
                    current_sequence += 1
                if current_sequence > result:
                    result = current_sequence
        return result