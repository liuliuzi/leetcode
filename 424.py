
class Solution(object):
    def characterReplacement(self, s, k):
        lenth=len(s)
        start = 0 
        end = 0
        ret=0
        while start + 1 < lenth and end < lenth:
            end=start
            flag=k
            firstDiff=0
            while flag >=0:
                if end +1 == lenth:
                    break                
                end=end+1 
                if s[start]!= s[end]:
                    if k==flag:
                        firstDiff=end 
                    flag=flag-1                
            ret=max(end-start,ret)
            start=firstDiff

        return ret



sol=Solution()
print sol.characterReplacement("AABABBA", 1)
