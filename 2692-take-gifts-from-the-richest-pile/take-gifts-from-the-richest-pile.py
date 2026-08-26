import math
from typing import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int: 
        max_heap= [-g for g in gifts]
        heapq.heapify(max_heap)
        for _ in range(k):
            largest = -heapq.heappop(max_heap)
            rem = int(isqrt(largest))
            heapq.heappush(max_heap, -rem)

        return -sum(max_heap)

            

        