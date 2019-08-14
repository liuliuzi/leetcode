class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        ppp = nums[-3] * nums[-2] * nums[-1]
        pnn = nums[0] * nums[1] * nums[-1]
        return max(ppp, pnn)

sol=Solution()
print sol.maximumProduct([1,2,3,4])
print sol.maximumProduct([-6,-4,1,2,3,4])
print sol.maximumProduct([-6,0,1,2,3,4])

