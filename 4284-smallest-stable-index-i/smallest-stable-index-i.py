class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            if self.max_sum(0,i,nums) - self.min_sum(i,len(nums)-1, nums) <= k:
                return i
        
        return -1 
    def max_sum(self,i1,i2,nums):
        max_sum = nums[i1]
        for i in range(i1,i2+1):
            max_sum = max(max_sum, nums[i])
        return max_sum

        
    def min_sum(self,i1,i2,nums):
        min_sum = nums[i1] 
        for i in range(i1,i2+1):
            min_sum = min(min_sum, nums[i])
        return min_sum
    
