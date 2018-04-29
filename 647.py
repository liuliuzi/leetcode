class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        i=0
        while i<len(s):
            j=0
            while i-j>=0 and i+j<len(s) and s[i-j]==s[i+j]:
                j=j+1
                count=count+1
            j=0
            while i-j-1>=0 and i+j<len(s) and s[i-j-1]==s[i+j]:
                j=j+1
                count=count+1
            i=i+1
        return count

sol=Solution()
print sol.countSubstrings("asdd")