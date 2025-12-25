class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        if strs[0] == "":
            return ""
        p = ""
        p2 = strs[0][0]
        for i in range(len(strs[0])):
            p2 = strs[0][i]
            f = True 
            for j in range(len(strs)):
                if i >= len(strs[j]) or p2 != strs[j][i]:
                    return p
            p += p2
        return p