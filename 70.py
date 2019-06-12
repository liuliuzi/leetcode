class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #f(n)=f(n-1)+f(n-2)
        #f(1)=1
        #f(2)=2
        #f(n),f(n-1)=f(n-1)+f(n-2),f(n-1)
        a = b = 1
        for i in range(n-1):
            a, b = a + b, a

        return a