class Solution(object):
    def combinations(self, n, k):
        if n < k or k < 1:
            return False
        retArry=[]
        rawArry=[]
        for x in xrange(n):
            rawArry.append(x+1)

        return self.combination(rawArry, k)

    def combination(self, rawArry, k):
        if k==1:
            newList=[]
            for x in rawArry:
                newList.append([x])
            return newList
        else:
            newList=[]
            for index in range(len(rawArry)):
                newrawArry=rawArry[0:index]
                newrawArry.extend(rawArry[index+1:])
                tt= self.combination(newrawArry,k-1)
                #print "tt:",tt, "index:", rawArry[index]
                for t in tt:
                    newt=t[:]
                    newt.append(rawArry[index])
                    #print "newt:",newt
                    newList.append(newt)
                #rawArry[index]                
            return newList

    def combine(self, n, k):
        def dfs(start, valuelist):
            print "dfs","start",start,"valuelist",valuelist
            if self.count == k: ret.append(valuelist); return
            for i in range(start, n + 1):
                self.count += 1
                dfs(i + 1, valuelist + [i])
                self.count -= 1
        ret = []; self.count = 0
        dfs(1, [])
        return ret




    
sol=Solution()
#print sol.combinations(5,3)
print sol.combine(5,3)

