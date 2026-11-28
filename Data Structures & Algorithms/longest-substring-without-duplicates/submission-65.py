class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left, right = 0, 0
        result = 0 
        hashing = set()

        while right < len(s):
            while s[right] in hashing:
                hashing.remove(s[left])
                left += 1
            hashing.add(s[right])
            right += 1
            result = max(result, len(hashing))
        return result
