class Solution(object):
    def minMeetingRooms(self, v):
        v.sort(key = lambda val: val.start)
        vMap={}
        for m in v:
            if  vMap.has_key(m.start):
                vMap[m.start]=vMap[m.start]+1
            else:
                vMap[m.start]=1
            if  vMap.has_key(m.end):
                vMap[m.end]=vMap[m.end]-1
            else:
                vMap[m.end]=-1

        ans = 0
        sum = 0
        for k,v in vMap:
            sum += v
            ans = max(ans, sum)
        return ans
        
