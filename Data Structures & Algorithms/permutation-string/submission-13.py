class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #hash the s1
        table_1 = []
        for i in range(26):
            table_1.append(0)
        for i in range(len(s1)):
            table_1[ord(s1[i]) - ord("a")] += 1

        left = 0
        right = left + len(s1) - 1
        while right <= len(s2) - 1:
            table_2 = []
            for i in range(26):
                table_2.append(0)
            for i in range(left, right + 1):
                table_2[ord(s2[i]) - ord("a")] += 1
            if table_1 == table_2:
                return True
            else:
                left += 1
                right += 1
        return False

        
        