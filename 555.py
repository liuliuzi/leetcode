class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = [max(s, s[::-1]) for s in strs]
        print(strs)
        ans = ''
        for i, st in enumerate(strs):
            left, right = ''.join(strs[:i]), ''.join(strs[i+1:])
            for s in (st, st[::-1]):
                for j in range(len(s)):
                    ans = max(ans, s[j:] + right + left + s[:j])
        return ans

sol=Solution()
print(sol.splitLoopedString(["abc", "xyz"]))