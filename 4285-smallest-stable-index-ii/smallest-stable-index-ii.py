class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        if n == 0 :
            return -1 
        suffsex_min = [0] * n
        suffsex_min[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            suffsex_min[i] = min(nums[i], suffsex_min[i+1])
        prefix_maxxx = nums[0]
        for i in range(n):
            prefix_maxxx = max(nums[i], prefix_maxxx)
            if prefix_maxxx - suffsex_min[i] <= k:
                return i
        return -1 


        