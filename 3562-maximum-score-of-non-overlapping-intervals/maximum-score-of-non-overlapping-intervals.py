class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervalsi = {}
        for i , (l,r,w) in enumerate(intervals):
            if not (l,r,w) in intervalsi: intervalsi[(l,r,w)] = i 
        intervals = sorted(intervalsi)
        n = len(intervals)
        @cache
        def dp(i, rem):
            if rem == 0 or i ==n:
                return 0, []
            #skip
            skipw, skip_ind = dp(i+1, rem)
            #take
            l, r, w = intervals[i]
            nexti =  bisect.bisect_left(intervals, (r+1,))
            nextw, next_ind = dp(nexti, rem -1 )
            takew = w + nextw
            take_ind = next_ind +  [intervalsi[intervals[i]]]
            take_ind.sort()
            if takew > skipw:
                return (takew, take_ind)
            elif takew < skipw:
                return (skipw, skip_ind)
            #tie ho gya
            if take_ind < skip_ind:
                return (takew, take_ind)
            else:
                return (skipw, skip_ind)
        return dp(0,4)[1]
