class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0 
        curr_sum = 0 
        maxii = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            while (r-l + 1) * nums[r] - curr_sum > k:
                curr_sum -= nums[l]
                l += 1
            maxii = max(r-l+1, maxii)
        return maxii
