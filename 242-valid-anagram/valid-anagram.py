class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Sorts = "".join(sorted(s))
        Sortt = "".join(sorted(t))
        if Sorts == Sortt:
            return True 
        return False 
        
        