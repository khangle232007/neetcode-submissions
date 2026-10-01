class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table_s = []
        for i in range(26):
            table_s.append(0)
        for i in range(len(s)):
            index = ord(s[i]) - ord("a")
            table_s[index] += 1

        
        table_t = []
        for j in range(26):
            table_t.append(0)
        for j in range(len(t)):
            index = ord(t[j]) - ord("a")
            table_t[index] += 1 

        if (table_s == table_t):
            return True
        else:
            return False
        





        

