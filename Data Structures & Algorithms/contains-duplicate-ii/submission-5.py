class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashing = {}
        for i in range(len(nums)):
            if (nums[i] in hashing) and (i - hashing[nums[i]] <= k):
                return True
            hashing[nums[i]] = i
        return False
