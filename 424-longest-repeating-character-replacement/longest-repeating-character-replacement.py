class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        n = 0
        m = 0
        d = {}
        while j < len(s):
            d[s[j]] = 1 + d.get(s[j], 0)
            n = max(n, d[s[j]])

            while (j-i+1) - n > k:
                d[s[i]] -= 1
                i+=1

            m = max(m, j-i+1)
            j +=1

        return m

        