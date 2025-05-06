def isValid(self, s: str) -> bool:
    stack = list()
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{':
            stack.append(ch)
            continue
        if len(stack):
            curr = stack.pop()
            if (curr == '(' and ch != ')'
                    or curr == '[' and ch != ']'
                    or curr == '{' and ch != '}'):
                return False
        else:
            return False
    if len(stack):
        return False
    return True