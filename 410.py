class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        f=[[0]*(m+1) for i in range(n+1)]
        sub=[0]*(n+1)
        i=0
        while  i < n:
            sub[i + 1] = sub[i] + nums[i]
            i=i+1
        print sub
        
        f[0][0] = 0
        i=1
        while i <= n:
            j=1
            while j <= m :
                k=0
                while k < i:
                    f[i][j] = min(f[i][j], max(f[k][j - 1], sub[i] - sub[k]))
                    k=k+1
                j=j+1
            i=i+1
        print f

        return f[n][m]
sol = Solution()
print sol.splitArray([1,2,3,4,5],2)
