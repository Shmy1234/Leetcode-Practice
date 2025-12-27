class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)//2
        for i in range(l):
            i2 = len(s) - 1 - i
            s[i], s[i2] = s[i2], s[i]
        