class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        if n <= 999:
            count = 0
        if n >= 1000:
            count = n - 1000 +1
        if n >= (10**6):
            count = n - (10*6) + 1
        return count      