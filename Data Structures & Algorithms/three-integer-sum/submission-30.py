class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            else:
                while left < right:
                    if nums[i] + nums[left] + nums[right] == 0:
                        triplet = []
                        triplet.append(nums[i])
                        triplet.append(nums[left])
                        triplet.append(nums[right])
                        result.append(triplet)
                        left += 1
                        right -= 1
                        while nums[left] == nums[left - 1] and left <= right - 1:
                            left += 1
                        while nums[right] == nums[right + 1] and right >= left + 1:
                            right -= 1          
                    elif nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    elif nums[i] + nums[left] + nums[right] < 0:
                        left += 1

        return result