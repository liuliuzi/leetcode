class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N==0: return 0
        pre = 1
        ppre = 0
        for i in range(1,N):
            pre,ppre =  pre+ppre,pre
        return pre
