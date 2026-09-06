class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        m = 0
        hashset = set()
        while j < len(s):
            if s[j] not in hashset:
                hashset.add(s[j])
                m = max(m, j - i + 1)
                j+=1
            else:
                while s[j] in hashset:
                    hashset.remove(s[i])
                    i+=1
        return m

            