class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        longest = 0
        substring = set()
        while j <= len(s) - 1:
            if s[j] in substring:
                substring.remove(s[i])
                i += 1
            else:
                substring.add(s[j])
                j+=1
            longest = max(longest, len(substring))
        return longest
            