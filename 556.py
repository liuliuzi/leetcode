class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = list(str(n))
        n = len(nums)
        i = n - 1
        while i > 0 and nums[i] <= nums[i - 1]:
            i -= 1
        if i == 0:
            return -1
        self.reverse(nums, i, n - 1)
        nums[i: n - 1]=nums[n-2:i-1,:-1]
        for j in range(i, n):
            if nums[j] > nums[i-1]:
                nums[i-1], nums[j] = nums[j], nums[i-1]
                break
        ans = int("".join(nums))
        if ans > 1 << 31:
            return -1
        else:
            return ans
