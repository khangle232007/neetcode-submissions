class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_s = {}
        table_t = {}
        for i in s:
            if i not in table_s:
                table_s[i] = 1
            else:
                table_s[i] += 1
        
        for i in t:
            if i not in table_t:
                table_t[i] = 1
            else:
                table_t[i] += 1
                
        return table_s == table_t
        