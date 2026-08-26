import math
from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int: 
        for _ in range(k):
            max_gif = max(gifts)
            indesex= gifts.index(max_gif)
            gifts[indesex] = math.isqrt(max_gif)
        return sum(gifts)
            

        