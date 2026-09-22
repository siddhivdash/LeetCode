class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        sett = set(nums)
        count = 0 
        for i in sett:
            if i - 1 not in sett:
                curr_num = i
                curr_count = 1
                while curr_num + 1 in sett:
                    curr_count += 1
                    curr_num += 1
                count = max(count,curr_count)
        return count