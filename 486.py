class Solution(object):
    nums=None
    sum2a=None
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        '''f(i,j)=max(numes[i]+sum2a[i+1][j]-f(i+1,j),numes[j]+sum2a[i][j-1]-f(i,j-1))   (j>i)
           f(i,j)= sum[i] (j=i)'''
        self.nums=nums
        total = sum(nums)
        sum2a = [[0 for i in range(len(nums))]for i in range(len(nums))]
        i=0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sum2a[i][j] = sum(nums[:j+1]) - sum(nums[:i])
        
        self.sum2a=sum2a
        print self.nums
        print self.sum2a
        sum1=self.f(0,len(nums)-1)
        return sum1


    def f(self,i,j):
        if i>j:
            return self.f(j,i)
        if i==j:
            return self.nums[i]
        x=self.nums[i]+self.sum2a[i+1][j]-self.f(i+1,j)
        y=self.nums[j]+self.sum2a[i][j-1]-self.f(i,j-1)
        return 2*sum1>=total


sol=Solution()
print sol.PredictTheWinner([2, 7, 11, 15])
print sol.PredictTheWinner([1,5,2])
print sol.PredictTheWinner([1,5,233,7])