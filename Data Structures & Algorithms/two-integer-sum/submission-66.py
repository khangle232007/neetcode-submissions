class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """ 
        1/ need map
        2/ loop 
        3/ find second num
        4/ if sec num not in hashing
                add current num and index
            elif sec num in hashing
                return hashing[current num], hashing[second num]


        """
        hashing = {}
        result =[]
        for i in range(len(nums)):
            second_num = target - nums[i]
            if second_num not in hashing:
                hashing[nums[i]] = i
            else:
                result.append(hashing[second_num])
                result.append(i)
        return result



    