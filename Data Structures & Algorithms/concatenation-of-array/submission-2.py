class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        answer = nums
        for i in range(len(nums)):
            answer.append(nums[i])
        return answer