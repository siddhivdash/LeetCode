class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        nums = ("".join([str(num) for num in digits]))
        settt = set()
        count =0
        for i in range(len(nums)):
            if nums[i] == "0":
                continue
            for j in range(len(nums)):
                if j == i:
                    continue
                for k in range(len(nums)):
                    if k== j or k == i:
                        continue
                    evens =  int( nums[i]+ nums[j] + nums[k] )
                    if evens % 2 == 0:
                        settt.add(evens)
                    
        return len(settt)
        


        