class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #val=max(list[i],val+list[i]);
        sumval=0
        val=0
        for node in nums:
            val=max(node,val+node);
            sumval=max(sumval,val);
        return sumval;

sol=Solution()
print sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])