class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['-','+','*','/']
        for tok in tokens:
            if tok not in operations:
                stack.append(int(tok))
            else:
                print(stack)
                print(tok)
                if tok == '-':
                    stack[-2] = stack[-2] - stack[-1]
                    stack.pop()
                elif tok == '+':
                    stack[-2] = stack[-2] + stack[-1]
                    stack.pop()
                elif tok == '*':
                    stack[-2] = stack[-2] * stack[-1]
                    stack.pop()
                elif tok == '/':
                    stack[-2] = int(stack[-2] / stack[-1])
                    stack.pop()
        return stack[0]