class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        has_zero = False 
        p = 1
        for n in nums: 
            if has_zero and n == 0:
                return [0]*len(nums)
            elif n == 0:
                has_zero=True 
            else:
                p*=n
        
        l = []
        for n in nums: 
            if has_zero and n!=0:
                l.append(0)
            elif has_zero and n==0:
                l.append(p)
            else:
                l.append(p//n)
        
        return l

