class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums is None:
            return []
        res = [[]]
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        for i in xrange(index, len(nums)):
            res.append(path + [nums[i]])
            path.append(nums[i])
            self.dfs(nums, i+1, path, res)
            path.pop()


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = [[]]
        for x in nums:
            with_x = []
            for s in result:
                with_x.append(s + [x])
            result = result + with_x
        return result

sol=Solution2()
print sol.subsets([1,2,3,4])