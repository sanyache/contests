class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = list()
        rez = ""
        for ch in s:
            if ch == '(':
                stack.append(ch)
                if len(stack) > 1:
                    rez += '('
                continue
            if len(stack) == 1:
                stack.pop()
            elif len(stack)>1:
                rez += ')'
                stack.pop()
        return rez
