class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        num=0
        i=j=0
        i=1
        exist=False
        #print len(A)
        while i<(len(A)-1):
            if A[i+1]-A[i]==A[i]-A[i-1]:
                exist=True
                break
            i=i+1
        if exist==False:
            return 0
        #print i

        i=i-1
        
        while i<(len(A)-2) and j<len(A):
            j=i+2
            subVal=A[i+1]-A[i]
            print "====0===",i,j
            while j<len(A):
                if A[j]-A[j-1]==subVal:
                    newadd=j-i-1
                    print "====",i,j,newadd
                    num=num+newadd
                    j=j+1
                    print "====1===",i,j
                else:
                    i=j
                    print "====2===",i,j
                    break
            #i=i+1              
        return num


sol=Solution()
print sol.numberOfArithmeticSlices([1, 2, 3, 4])
