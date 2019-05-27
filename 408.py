class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        k = 0
        i = 0
        len1 = len(word)
        len2 = len(abbr) 
        while i < len2:
            if(word[k]==abbr[i]):
                i=i+1
                k=k+1
                continue
            cnt = 0
            if abbr[i] == '0':
                return False
            while abbr[i]>='0' and abbr[i]<='9':
                cnt = cnt*10 + ord(abbr[i])-ord('0')
                i=i+1
            k += cnt
            if k > len1 or word[k] != abbr[i]:
                return False

        return k==len1

sol=Solution()
print sol.validWordAbbreviation("internationalization", "i12iz4n")
