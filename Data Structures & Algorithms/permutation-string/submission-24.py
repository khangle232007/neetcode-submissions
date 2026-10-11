class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #hash the s1
        table_1 = [0] * 26
        table_2 = [0] * 26
        for i in range(len(s1)):
            table_1[ord(s1[i]) - ord("a")] += 1

        left = 0
        right = left + len(s1) - 1

        for i in range(left, right + 1):
                table_2[ord(s2[i]) - ord("a")] += 1

        while right <= len(s2) - 1:
            if table_1 == table_2:
                return True
            else:
                if right == len(s2) - 1:
                    break
                table_2[ord(s2[left]) - ord("a")] -= 1
                left += 1
                right += 1
                table_2[ord(s2[right]) - ord("a")] += 1
        return False

        
        