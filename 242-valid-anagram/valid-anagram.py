class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ls = [0]*26
        lt = [0]*26
        for c in s:
            ls[ord(c) - ord('a')] += 1
        for c in t: 
            lt[ord(c) - ord('a')] += 1
        print(ls, lt)
        return ls == lt