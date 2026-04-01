class Solution:
    def isValid(self, s: str) -> bool:
        closed = dict({')':'(', '}':'{', ']':'['})
        if len(s) % 2 != 0:
            return False
        stack = []
        for c in s:
            if c in closed:
                if stack and stack[-1] == closed[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
        