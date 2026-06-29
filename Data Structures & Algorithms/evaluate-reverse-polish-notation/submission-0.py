class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+", "-", "*", "/"}
        for tok in tokens:
            if tok in ops:
                y = stack.pop()
                x = stack.pop()
                current = 0

                if tok == "+":
                    current = x + y
                elif tok == "-":
                    current = x - y
                elif tok == "*":
                    current = x * y
                else:
                    current = int(x/y)
                stack.append(current)
            else:
                stack.append(int(tok))
        return stack.pop()
    