class Solution(object):
    '''
    f(x)=f(x-1) +-1 
    '''
    def inScope(self,step,num):
        if step==num or step==num+1 or step==num-1:
            return True
        else: 
            return False

    def helper(self, arr, nextStep):
        #print "helper",arr, nextStep
        if len(arr)==2 and  self.inScope(nextStep,arr[1]-arr[0]):
            #print "helper result True"
            return True
        else:
            ret=False
            lenth=len(arr)
            i=2
            while i<lenth and arr[-i] > arr[-1]-nextStep-1:
                if arr[-1]-nextStep==arr[-i]:
                    ret=ret or self.helper(arr[0:-i+1], arr[-1]-arr[-i])
                elif arr[-1]-nextStep+1==arr[-i]:
                    ret=ret or self.helper(arr[0:-i+1], arr[-1]-arr[-i]) 
                elif arr[-1]-nextStep-1==arr[-i]:
                    ret=ret or self.helper(arr[0:-i+1], arr[-1]-arr[-i]) 
                i=i+1 
            #print "helper result for" ,arr, nextStep, ret
            return ret


    def canCross(self, arr):
        i=1
        #print "start",arr
        while i<len(arr):
            step=arr[-1]-arr[-(i+1)]
            if self.helper(arr[0:-i],step)==True:
                return True
            i=i+1
        return False



    def print2DArr(self, arr):
        for raw in arr:
            print raw
    def canCross2(self, arr):
        i=1
        print "start",arr
        lenth=len(arr)
        stepArr=[]
        i=j=0
        while i<lenth:
            j=0
            while j<lenth:
                if i>=j:
                    if len(stepArr)<=i:
                        stepArr.append([arr[i]-arr[j]])
                    else:
                        stepArr[i].append(arr[i]-arr[j])
                else:
                    break
                j=j+1
            i=i+1
        self.print2DArr(stepArr)

        i=2
        while i<lenth:
            j=0
            retVal =False
            while j<i:
                if j==0:
                    #if self.inScope(stepArr[i][j],stepArr[i-1][j]):


                j=j+1

            i=i+1 

        return True


sol=Solution()
print sol.canCross2([0,1,3,5,6,8,12,17])
print sol.canCross2([0,1,2,3,4,8,9,11])
