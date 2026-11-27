class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = []
        result = []
        for i in range(len(nums) + 1):
            freq.append([])
        
        for i in nums:
            count[i] += 1

        for i, j in count.items():
            freq[j].append(i)

        for i in range(len(freq) - 1, 0, -1):
            # loop through each element of 1 bracket
            for j in freq[i]:
                result.append(j)
                if len(result) == k:
                    return result       