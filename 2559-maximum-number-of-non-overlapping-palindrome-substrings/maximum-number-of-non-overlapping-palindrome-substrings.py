class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        start =0 
        for i in range(n):
            for l,r in ((i,i), (i,i+1)):
                while l >= start and r < n and s[l] == s[r]:
                    lenn = r -l + 1
                    if lenn >= k:
                        ans += 1
                        start = r + 1
                    l -= 1
                    r += 1
        return ans