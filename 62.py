#martix[i][j] = martix[i - 1][j] + martix[i][j - 1]

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        martix = [[0] * n] * m
        for i in range(m):
            for j in range(n):
                if j == 0 or i == 0:
                    martix[i][j] = 1
                else:
                    martix[i][j] = martix[i - 1][j] + martix[i][j - 1]
        return martix[m - 1][n - 1]


sol=Solution()
print sol.uniquePaths(3,7)
