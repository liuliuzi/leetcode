class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.add = [0]
        for i in nums:
            self.add.append(self.add[-1] + i)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.add[j+1] - self.add[i]