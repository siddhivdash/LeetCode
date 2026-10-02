class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx_sum = nums[0]
        curr_sum = 0
        for i in nums:
            curr_sum += i
            if curr_sum > maxx_sum:
                maxx_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0 
        return maxx_sum

            


        