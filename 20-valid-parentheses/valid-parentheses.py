class Solution:
    def isValid(self, s: str) -> bool:
        tracker = {')': '(', ']': '[', '}': '{'}
        lst = []
        for char in s:
            if char in ")]}":
                if len(lst) != 0 and lst[-1] == tracker[char]:
                    lst.pop()
                else: 
                    return False
            elif char in "([{":
                lst.append(char)
        
        return True if len(lst) == 0 else False