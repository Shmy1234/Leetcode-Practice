class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) -1 
        while i <= j:
            p = ((j + i) // 2)
            if nums[p] > target:
                j = p-1 
            elif nums[p] < target:
                i = p+1
            else:
                return p
        
        return -1
