class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        cnt1 = 0 
        cnt2 = 0 
        elem1 = None 
        elem2 = None 
        for i in nums:
            if i == elem1:
                cnt1 += 1
            elif i == elem2:
                cnt2 += 1
            elif cnt1 == 0:
                elem1 = i
                cnt1 = 1
            elif cnt2 ==0 :
                elem2 = i
                cnt2 = 1
            
            else:
                cnt1 -= 1 
                cnt2 -= 1
        threshold = len(nums) //3 
        res = []
        for i in (elem1, elem2):
            if i is not None and nums.count(i) > threshold:
                res.append(i)
        return res
        