class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in ("+", "-", "*", "/"):
                stack.append(tokens[i])
            elif tokens[i] == "+":
                result = int(stack[-2]) + int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == "-":
                result = int(stack[-2]) - int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == "*":
                result = int(stack[-2]) * int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == "/":
                result = int(stack[-2]) / int(stack[-1])
                stack.pop()
                stack.pop()
                stack.append(result)
        return int(stack[-1])
