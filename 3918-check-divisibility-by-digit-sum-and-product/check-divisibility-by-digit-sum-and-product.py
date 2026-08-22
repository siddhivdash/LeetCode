class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        i = n 
        s=0
        p =1
        while i != 0:
            s += (i % 10)
            p *= (i % 10)
            i //= 10 
        ss = s + p
        if n % ss == 0:
            return True
        else:
            return False
        