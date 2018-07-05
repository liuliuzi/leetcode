class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = len(t)
        minileft = 0
        miniSize = len(s) + 1
        left = 0
        cmap = {}
        for c in t:
            if c not in cmap:
                cmap[c] = 1
            else:
                cmap[c] += 1
        #print cmap

        for right in range(len(s)):
            if s[right] in cmap:
                cmap[s[right]] -= 1
                if cmap[s[right]] >= 0:
                    count -= 1
                if count == 0:
                        print cmap
                        print right,s[right]
                        while True:
                            if s[left] in cmap:
                                if cmap[s[left]] < 0:
                                    cmap[s[left]] += 1
                                else:
                                    break 
                            left += 1

                        if right - left + 1 < miniSize:
                            minileft = left
                            miniSize = right - minileft + 1

        if miniSize < len(s) + 1:
            return s[minileft:minileft + miniSize]
        else:
            return ''


sol=Solution()
print sol.minWindow("ADAOBECODAEBANC","AABC")
