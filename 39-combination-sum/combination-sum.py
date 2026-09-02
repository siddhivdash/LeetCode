class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        arr = []
        self.bhadwa(0, target, nums, res, arr)
        return res
    
    def bhadwa(self, pos, target, nums,res, arr):
        if pos == len(nums) or target < 0:
            return
        if target == 0:
            res.append(list(arr))
            return

        if nums[pos] <= target:
            arr.append(nums[pos])
            self.bhadwa(pos, target - nums[pos], nums, res, arr)
            arr.pop()
        self.bhadwa(pos+1 , target, nums,res, arr)

        


        