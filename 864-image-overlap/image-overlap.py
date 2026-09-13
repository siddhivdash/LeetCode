class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)

        one1 = [(r,c) for r in range(n) for c in range(n) if img1[r][c] == 1]
        one2 = [(r,c) for r in range(n) for c in range(n) if img2[r][c] == 1]
        if not one1 or not one2:
            return 0 
        shifts = Counter()
        for r1,c1 in one1:
            for r2,c2 in one2:
                diff = (r2-r1, c2-c1)
                shifts[diff] +=1 

        return max(shifts.values())

        