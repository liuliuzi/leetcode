class Solution:
    def findMaximizedCapital(self, k, w, Profits, Capital):
        pur=[]
        for i in range(len(Profits)):
            pur.append(Profits[i]-Capital[i])
        for _ in range(k):
            index=None
            maxpur=0
            for i in range(len(Profits)):
                if w >= Capital[i]:
                    if pur[i]>maxpur:
                        maxpur=pur[i]
                        index=i
                else:
                    continue
            if index==None:
                break
            else:
                Capital[index]=100000
            w+=Profits[index]        
        return w

    def findMaximizedCapital1(self, k, W, Profits, Capital):
        num=[x for x in zip(Profits,Capital)]
        num.sort()
        print num
        while k and num:
            i=len(num)-1
            while i>=0 and num[i][1]>W:
                i-=1
            if i<0:
                break
            W+=num[i][0]
            num.pop(i)
            k-=1
        return W
sol=Solution()
print sol.findMaximizedCapital1(2, 0, [1,2,3], [0,1,1])