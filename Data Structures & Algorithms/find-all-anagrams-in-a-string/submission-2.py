class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:    
        result = []
        if  len(p) > len(s): 
            return result
        pDict, sDict = {}, {}

        for i in range(len(p)):
            pDict[p[i]] = pDict.get(p[i], 0) + 1
            sDict[s[i]] = sDict.get(s[i], 0) + 1
        
        if pDict == sDict:
            result.append(0)

        left = 0
        for right in range(len(p), len(s)):
            sDict[s[left]] -= 1
            if sDict[s[left]] == 0:
                del sDict[s[left]]
            left += 1
            sDict[s[right]] = sDict.get(s[right], 0) + 1
            if sDict == pDict:
                result.append(left)           
        return result