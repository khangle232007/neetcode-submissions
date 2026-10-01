class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        diction = {}
        for i in range(len(nums)):
            second = target - nums[i]
            if second not in diction:
                diction[nums[i]] = i
            elif second in diction:
                result.append(diction[second])
                result.append(i)
                return result


    