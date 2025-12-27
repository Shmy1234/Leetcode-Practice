class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        d = {}
        for n in nums:
            if n-1 in d:
                d[n] = d[n-1] + 1
            else:
                d[n] = 1
        l = list(d.values())
        if not l: 
            return 0
        return max(l)