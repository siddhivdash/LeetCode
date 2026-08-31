from collections import Counter
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = sorted(set(nums), reverse = True)
        
        if len(unique) >= 3:
            return unique[2]
        return unique[0]
            
        

            

        