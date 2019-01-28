class Solution(object):
    def canAttendMeetings(self, v):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        v.sort(key = lambda val: val.start)
        return not any(v[i].start < v[i-1].end for i in range(1,len(v)))