class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for word in strs:
            l = [0]*26
            for char in word:
                l[ord(char) - ord('a')] += 1 
            d[tuple(l)] = [word] + d.get(tuple(l), [])
        return list(d.values())