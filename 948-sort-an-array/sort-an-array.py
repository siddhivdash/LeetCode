class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        def countingsort():
            count = defaultdict(int)
            minval = min(nums)
            maxval = max(nums)
            for val in nums:
                count[val] += 1
            index = 0 
            for val in range(minval, maxval + 1):
                while count[val] > 0:
                    nums[index] = val
                    index += 1
                    count[val] -= 1
        countingsort()
        return nums

        