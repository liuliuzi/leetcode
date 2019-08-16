'''Example 1:
Input: [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:

Input: [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]'''
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        start=0
        end=None
        retVal=[]
        for index in range(1,len(nums)):
            if nums[index]!=nums[index-1]+1:
                end=index-1
                if end==start:
                    retVal.append(str(nums[start]))
                else:
                    retVal.append(str(nums[start])+"->"+str(nums[end]))

                start=index

        if len(nums)==start+1:
            retVal.append(str(nums[start]))
        else:
            retVal.append(str(nums[start])+"->"+str(nums[-1]))
        return retVal

sol=Solution()
print sol.summaryRanges([0,2,3,4,6,8,9])
print sol.summaryRanges([0,1,2,4,5,7])
