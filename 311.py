class Solution(object):
    def arrTrans(self,a):
        retArr=[]
        lenth= len(a)
        i=0
        jlenth= len(a[0])
        j=0
        while i<lenth:
            j=0
            while j<jlenth:
                if i==0:
                    retArr.append([a[i][j]])
                else:
                    retArr[j].append(a[i][j])
                j=j+1
            i=i+1
        return retArr

    def multiplication(self, a , b):
        resArry=[]
        for row in a:
            resRow=[]
            for col in self.arrTrans(b):
                eleSum=0
                lenth= len(row)
                i=0
                while i<lenth:
                    eleSum=eleSum+row[i]*col[i]
                    i=i+1
                resRow.append(eleSum)
            resArry.append(resRow)
        return  resArry
        
sol=Solution()
a=[
  [ 1, 0, 0],
  [-1, 0, 3]
]
b=[
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
#print sol.arrTrans(a)
print sol.multiplication(a,b)
