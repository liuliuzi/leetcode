class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: return 0
        intervals.sort()
        last = 0
        res = 0
        for i in range(1, len(intervals)):
            if intervals[last][-1] > intervals[i][0]:
                if intervals[i][-1] < intervals[last][-1]:
                    last = i
                res += 1
            else:
                last = i
        return res
sol=Solution()
print(sol.eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3] ]))