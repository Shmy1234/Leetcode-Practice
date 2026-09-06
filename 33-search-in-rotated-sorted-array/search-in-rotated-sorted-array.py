class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i<=j:
            p = (j+i)//2
            if target == nums[p]:
                return p

            if nums[i] <= nums[p]:
                if nums[i] <= target < nums[p]:
                    j = p - 1
                else:
                    i = p + 1
            else:
                if nums[p] < target <= nums[j]:
                    i = p + 1
                else:
                    j = p - 1

        return -1
        
            
