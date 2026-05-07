class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == ')':
                if stack:
                    x = stack.pop()
                else:
                    return False
                if x != '(':
                    return False
            elif char == ']':
                if stack:
                    x = stack.pop()
                else:
                    return False
                if x != '[':
                    return False
            elif char == '}':
                if stack:
                    x = stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True
        