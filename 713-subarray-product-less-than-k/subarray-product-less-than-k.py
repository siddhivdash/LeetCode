class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        l = 0 
        prd = 1
        for r in range(len(nums)):
            prd *= nums[r]
            while l <= r and prd >= k:
                prd //= nums[l]
                l += 1
            res += (r - l + 1)
            
        return res 



        