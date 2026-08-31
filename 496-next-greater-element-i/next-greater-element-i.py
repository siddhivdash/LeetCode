class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}
        for i in nums2:
            while stack and i > stack[-1]:
                smaller_num = stack.pop()
                greater[smaller_num] = i
            stack.append(i)
        res = []
        for num in nums1:
            if num in greater:
                res.append(greater[num])
            else:
                res.append(-1)
        return res 


        

