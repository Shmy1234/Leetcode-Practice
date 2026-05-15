class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        hasZero = False
        for n in nums: 
            if n == 0 and hasZero: 
                return [0]*len(nums)
            elif n == 0:
                hasZero = True
            else: 
                p *= n
        
        l = []
        for n in nums: 
            if hasZero and n!=0:
                l.append(0)
            elif n==0:
                l.append(p)
            else: 
                l.append(p//n)
        return l