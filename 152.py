class Solution(object):
    def maxProduct(self, nums):
        '''
        dp[i][0] = min(min(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i]), nums[i]);
        dp[i][1] = max(max(dp[i - 1][0] * nums[i], dp[i - 1][1] * nums[i]), nums[i]);
        '''
        result = nums[0]
        minPro = nums[0]
        maxPro = nums[0]
        temp0 = temp1 = 0
        i=1

        while  i < len(nums):
            temp0 = minPro * nums[i]
            temp1 = maxPro * nums[i]

            minPro = min(min(temp0, temp1), nums[i])
            maxPro = max(max(temp0, temp1), nums[i])

            result = max(maxPro, result)

            i=i+1
        

        return result;



sol=Solution()
print sol.maxProduct([2,3,-2,4])
print sol.maxProduct([2,3,-2,4,-1])