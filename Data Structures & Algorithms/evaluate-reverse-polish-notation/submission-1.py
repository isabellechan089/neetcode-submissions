class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def recur():
            tok = tokens.pop()
            if tok not in "+-/*":
                return int(tok)
            
            y = recur()
            x = recur()
            current = 0
            if tok == "+":
                current = x + y
            elif tok == "-":
                current = x - y
            elif tok == "*":
                current = x * y
            else:
                current = int(x/y)
            return current
        
        return recur()
