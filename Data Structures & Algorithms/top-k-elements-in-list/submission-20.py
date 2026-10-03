class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        diction = {}
        result = []
        sorted_value = []
        # create a hash table for every numbers
        for i in range(len(nums)):
            if nums[i] not in diction:
                diction[nums[i]] = 0
            else:
                diction[nums[i]] += 1

        # take the most frequent values inside dictionary
        # sort the whole dictionary based on the key
        diction = sorted(diction, key = diction.get, reverse=True)   

        # get the actual number, not the index
        for i in range(k):
            result.append(diction[i])

        return result

