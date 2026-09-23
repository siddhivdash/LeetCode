class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while r >= l:
            mid = (r + l) // 2
            hrs_spent = 0
            for i in piles:
                hrs_spent += math.ceil(i/mid)
            if h >= hrs_spent:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans 
            
