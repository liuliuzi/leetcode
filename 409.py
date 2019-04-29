class Solution(object):
    def longestPalindrome(self, word):
        retVal=0
        charDict={}
        for node in word:
            if charDict.has_key(node):
                charDict[node]=charDict[node]+1
            else:
                charDict[node]=1
        flag=0
        print charDict
        for k,v in charDict.iteritems():
            if v%2!=0 and flag==0:
                retVal=retVal+1
                flag=1
            retVal=retVal+v/2
        return retVal

sol=Solution()
print sol.longestPalindrome("abccccdd")