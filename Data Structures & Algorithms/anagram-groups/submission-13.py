class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for word in strs:
            table = [0] * 26
            for char in word:
                table[ord(char) - ord("a")] += 1
            key = tuple(table)           
            result[key].append(word)
        return list(result.values())