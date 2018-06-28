class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen=0
        i=j=0
        while i<len(s) and j<len(s):
            j=i+1
            while j<len(s):
                if s[j] not in s[i:j]:
                    j=j+1
                else:
                    maxlen=max(maxlen,j-i)
                    jump=s[i:j].index(s[j])
                    i=i+1+jump                    
                    break
        return maxlen


sol=Solution()
print sol.lengthOfLongestSubstring("abcabcbb")