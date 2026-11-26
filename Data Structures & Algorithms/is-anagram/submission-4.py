class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_s = {}
        table_t = {}
        for i in range(len(s)):
            if (ord(s[i]) - ord("a")) not in table_s:
                table_s[ord(s[i]) - ord("a")] = 1
            else:
                table_s[ord(s[i]) - ord("a")] += 1
        
        for i in range(len(t)):
            if (ord(t[i]) - ord("a")) not in table_t:
                table_t[ord(t[i]) - ord("a")] = 1
            else:
                table_t[ord(t[i]) - ord("a")] += 1
        if table_s == table_t:
            return True
        else:
            return False
        