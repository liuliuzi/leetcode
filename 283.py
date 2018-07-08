class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i=j=0
        while i<len(nums)-1:
            if nums[i]==0:
                j=i+1
                while j<len(nums) and nums[j]==0  :
                    j=j+1
                if j<len(nums): 
                    nums[i]=nums[j]
                    nums[j]=0
            i=i+1
        return nums

        
sol=Solution()
print sol.moveZeroes([1, 0, 0,1,1, 0, 3, 12])
print sol.moveZeroes([0,1,0,3,12])