class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        res = nums[0]
        while i<=j:
            if nums[i]<nums[j]:
                res=min(res, nums[i])
                break 
            
            p = (j+i)//2
            res = min(res, nums[p])

            if nums[p] >= nums[i]:
                i=p+1
            else:
                j=p-1
        
        return res

        