class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1: return [strs]
        result = {}
        for word in strs:
            table = [0] * 26
            for char in word:
                table[ord(char) - ord("a")] += 1
            key = tuple(table)
            if key not in result:
                result[key] = []
                result[key].append(word)
            else:
                result[key].append(word)
        return list(result.values())
