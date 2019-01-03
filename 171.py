class Solution(object):
    def titleToNumber(self, s):
        sum=0
        for x in s:
            sum = sum*26+ord(x)-ord('A')+1
        return sum

sol=Solution()


print sol.titleToNumber("AB")