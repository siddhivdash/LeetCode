class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        x = len(haystack)
        y = len(needle)
        for i in range(x -y + 1 ):
            if haystack[i:y +i] == needle:
                return i 
        return -1