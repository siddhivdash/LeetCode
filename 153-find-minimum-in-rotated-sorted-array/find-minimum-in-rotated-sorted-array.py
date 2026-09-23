class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) -1
        while r > l:
            mid = (l+r)// 2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid 
        return nums[l]