class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        dictionary = {}
        for i in range(len(nums)):
            second_number = target - nums[i]
            if second_number not in dictionary:
                dictionary[nums[i]] = i 
            else:
                result.append(dictionary[second_number])
                result.append(i)
        return result