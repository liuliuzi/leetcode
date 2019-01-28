class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        rev_s = s[::-1]
        l = s + "#" +  rev_s
        p = [0] * len(l)
        print p,l
        for i in range(1,len(l)):
            j = p[i - 1]
            print i,j
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        print "====",p[i]
        print "====",len(s) - p[-1]
        print "!====!",rev_s[:len(s) - p[-1]]
        print "!====!",rev_s[:2]
        return rev_s[:len(s) - p[-1]] + s

sol=Solution()
print sol.shortestPalindrome("aabc")