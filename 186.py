class Solution(object):
    def revert(self,string):
        string=list(string[::-1])
        start=0
        end=0
        while end <= len(string):
            if end ==len(string) or string[end]== " ":
                tmpList=string[start:end]
                tmpList=tmpList[::-1]
                string[start:end]=tmpList
                start=end+1
            end=end+1
        return  ''.join(string)   

sol=Solution()
print sol.revert("the sky is blue")