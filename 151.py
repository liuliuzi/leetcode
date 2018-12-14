class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strList=s.split(" ")
        retStr=""
        lenth=len(strList)
        i=-1
        while i>= (0-lenth):
         	if  strList[i]!="":
         		if retStr!="":
         			retStr=retStr+" "
         		retStr=retStr+strList[i]
         	i=i-1
        return retStr


sol=Solution()


print sol.reverseWords(" the sky  is blue ")