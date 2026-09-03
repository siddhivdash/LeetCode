class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        l = 0 
        def small_pennis(max_diff):
            cnt = 0 
            i = 0 
            while i < len(nums) - 1:
                if nums[i+1] - nums[i] <= max_diff:
                    cnt += 1
                    i += 2
                else:
                    i +=1 
            return cnt >= p


        l = 0 
        r = nums[-1] - nums[0]
        ans = r 
        while r >= l:
            mid = (l+r) // 2
            if small_pennis(mid):
                ans = mid
                r= mid - 1
            else:
                l = mid + 1
        return ans 



        