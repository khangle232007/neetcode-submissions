class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashing = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in hashing:
                hashing.remove(s[left])
                left += 1
            hashing.add(s[right])
            result = max(result, right - left + 1)
        
        return result