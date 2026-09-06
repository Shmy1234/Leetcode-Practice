class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            j = i+1
            k = len(nums) - 1
            if nums[i]>0:
                break
            if i>0 and nums[i] == nums[i-1]:
                continue 
            
            while j < k:
                a = [nums[i], nums[j], nums[k]]
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append(a)
                    j+=1 
                    k-=1

                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
                elif s <0:
                    j+=1
                else:
                    k-=1
        return res