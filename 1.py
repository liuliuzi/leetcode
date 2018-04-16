class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictMap={}
        i=0
        for node in nums:
            dictMap[node]=i
            i=i+1
        i=0
        while i<len(nums) :
            if dictMap.has_key(target-nums[i]) and dictMap[target-nums[i]] != i:
                return [i,dictMap[target-nums[i]]]
            i=i+1


sol=Solution()
print sol.twoSum([2, 7, 11, 15],18)
print sol.twoSum([3, 2, 4],6)
