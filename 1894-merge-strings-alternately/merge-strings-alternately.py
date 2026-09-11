class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        ass = []
        i =j = 0
        while i < n and j < m:
            ass.append(word1[i])
            i+= 1
            ass.append(word2[j])
            j+= 1
        if i < n:
            ass.append(word1[i:])
        if j < m:
            ass.append(word2[j:])
        return "".join(ass)

        