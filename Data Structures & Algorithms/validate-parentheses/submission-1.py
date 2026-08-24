class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpenMap = { ')':'(', '}':'{', ']':'['}

        for char in s:
            if char in closeToOpenMap:
                if stack and stack[-1] == closeToOpenMap[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return True if not stack else False
        