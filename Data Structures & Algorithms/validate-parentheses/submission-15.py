class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")" or s[i] == "}" or s[i] == "]":
                if not stack:
                    return False
                if stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False 