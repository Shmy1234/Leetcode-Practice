class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(', ']':'[', '}':'{'}
        stack = []
        for c in s: 
            if c in "({[":
                stack.append(c)
            elif c in d:
                if stack and stack.pop() == d[c]:
                    continue
                else:
                    return False
        
        return stack == []
        