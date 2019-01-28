class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            # print nums[i], i + 1, nums[nums[i] - 1]
            while nums[i] > 0 and nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        # print nums
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1
        return n + 1


sol=Solution()
print sol.firstMissingPositive([3,4,-1,1])
print sol.firstMissingPositive([7,8,9,1])