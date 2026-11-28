class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashing = defaultdict(int)
        result = 0
        left, right = 0, 0 

        while right < len(s):
            hashing[s[right]] += 1
            
            while (right - left + 1) - max(hashing.values()) > k:
                hashing[s[left]] -= 1
                left += 1
            
            result = max(result, right - left + 1)
            right += 1
        return result