class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if (len(nums) <= 2) :
        	return False;
        n = len(nums)
        i = 0
        j = 0
        k = 0
        while i < n:
            while i < n - 1 and nums[i] >= nums[i + 1] :
            	i=i+1
            j = i + 1;
            while j < n - 1 and nums[j] <= nums[j + 1] :
            	j=j+1
            k = j + 1
            while (k < n):
                if nums[j] > nums[i] and nums[j] > nums[k] :
                	return True;
                k=k+1
            i = j + 1
        return False;

sol=Solution()
#print sol.find132pattern([2,3,1,4,5,4])
print sol.find132pattern([1,2,3])