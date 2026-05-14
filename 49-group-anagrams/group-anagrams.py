class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            l = [0]*26
            for c in s: 
                l[ord(c) - ord("a")] +=1 
            
            if tuple(l) in d:
                d[tuple(l)].append(s)
            else:
                d[tuple(l)] = [s]

        return list(d.values())