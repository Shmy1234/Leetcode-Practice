class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        m = 0
        hashset = set()
        while j < len(s):
            while s[j] in hashset:
                hashset.remove(s[i])
                i+=1
            m = max(m, j-i+1)
            hashset.add(s[j])
            j+=1 
        return m
            