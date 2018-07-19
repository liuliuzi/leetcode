class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        maxProfit=0
        minPurchase=prices[0]
        for price in prices:
        	maxProfit= max(maxProfit,price-minPurchase)
        	minPurchase=min(price,minPurchase)
        return maxProfit
sol=Solution()
print sol.maxProfit([2,3,1,4,5,4])
