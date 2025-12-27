class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = word1
        w2 = word2 
        s = ""
        while w1 and w2:
            s = s + w1[0] + w2[0]
            w1 = w1[1:]
            w2 = w2[1:]
        return s + w1 + w2