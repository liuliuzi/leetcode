class Solution:
    def wordsTyping(self, sentence, rows, cols):
        str=""
        for x in sentence:
            str += x + " "
        lenth = len(str)
        start = 0
        for i in  range(rows):
            start += cols
            if str[start%lenth]==' ':
                start+=1
                continue
            while start > 0 and str[(start-1)%lenth]!=' ':
                start-=1
        return start/lenth

sol=Solution()
print sol.wordsTyping(["a", "bcd", "e"],3,6)