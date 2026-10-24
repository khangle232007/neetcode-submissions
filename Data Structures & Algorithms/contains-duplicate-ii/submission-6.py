class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashing = {}
        for i, value in enumerate(nums):
            if (value in hashing) and (i - hashing[value] <= k):
                return True
            hashing[nums[i]] = i
        return False
