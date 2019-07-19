class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # s1 > s2 > s3
        s1, s2, s3 = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num > s1:
                s1, s2, s3 = num, s1, s2
            elif num < s1 and num > s2:
                s2, s3 = num, s2
            elif num < s2 and num > s3:
                s3 = num
        return s3 if s3 != float('-inf') else s1
