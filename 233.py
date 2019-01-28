class Solution(object):
    def countDigitOne(self, n):
        res = 0
        a = 1
        b = 1
        while (n > 0):
            res += (n + 8) / 10 * a + (n % 10 == 1) * b;
            b += n % 10 * a;
            a *= 10;
            n /= 10;
        return res
sol=Solution()
print sol.countDigitOne(12)