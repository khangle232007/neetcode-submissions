class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashing = {}
        for index, value in enumerate(nums):
            second_num = target - value
            if second_num not in hashing:
                hashing[value] = index
            else:
                return [hashing[second_num], index]