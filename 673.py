class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=j=maxlen=0
        while i<len(nums)-1:
            j=i+1
            if nums[j] >nums[j-1]:
                j=j+1
            



sol=Solution()
print sol.findNumberOfLIS([1, 0, 0,1,1, 0, 3, 12])
print sol.findNumberOfLIS([0,1,0,3,12])