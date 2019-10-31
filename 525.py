class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <=1:
            return 0
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        sumDict = {0:-1}
        sum = 0
        ret = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum in sumDict: # sum-before_sum=0 means sum[before_sum:sum]=0
                ret = max(ret,i-sumDict[sum])
            else:
                sumDict[sum] = i
        return ret
sol=Solution()
print(sol.findMaxLength([1,0,1,1,1,1,0]))