class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        m = 0
        d = {}
        for n in nums:
            if n > 1 and n in d:
                continue 
            if n > 1 and n-1 in d:
                d[n] = d[n-1] + 1
                m += 1
            elif n == 1:
                d[n] = 1
                m = 1
            elif n > 1:
                return m + 1
        return m + 1