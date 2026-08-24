class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+':lambda x, y: x + y,
            '-':lambda x, y: x - y,
            '*':lambda x, y: x * y,
            '/':lambda x, y: int(x / y)
        }
        res = 0
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = operations[token](num1, num2)
                stack.append(res)
        return stack[0]
