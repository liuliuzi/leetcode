class Solution(object):
    def convertToTitle(self, i):
        retStr=[]
        while i>0:
            leave=(i-1)%26
            i=(i-1)/26
            retStr.append(chr(ord('A')+leave)) 
        return "".join(retStr[::-1])

sol=Solution()


print sol.convertToTitle(288)