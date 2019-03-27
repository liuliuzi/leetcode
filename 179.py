class Solution(object):


    def large(self, num1, num2):
        num1str=str(num1)
        num2str=str(num2)
        return (num1str+num2str) >(num2str+num1str)
    
    def quick_sort(self,array, left, right):
        
        print  "quick_sort", array , left,   right
        if left >= right:
            return
        low = left
        high = right
        key = array[low]
        while left < right:
            while left < right and array[right] > key:
                right -= 1
            array[left] = array[right]
            print  "set1 array[",left,"]=",array[right]
            while left < right and array[left] <= key:
                left += 1
            array[right] = array[left]
            print  "set2 array[",right,"]=",array[left]
        array[right] = key
        print  "set3 array[",right,"]= key = ",key
        print  "low = " ,low ," left - 1=" , left - 1 , " left + 1=", left + 1, " high=", high
        self.quick_sort(array, low, left - 1)
        self.quick_sort(array, left + 1, high)

    def quickSort(self,nums,left,right):
        #print  "quickSort", nums , left,   right, "index=", nums[left]
        if left >= right:
            #print  " end this quickSort for  left >= right ", nums , left,   right
            return

        index=left
        end=right

        while left < right:
            #while nums[right] > nums[index] and left<right:
            while self.large(nums[right] , nums[index]) and left<right:
                #print "find right--", nums[right], " > ",nums[index],  nums[right] > nums[index]
                right = right -1
            #print "find left < index ,right=", right
            #while nums[left] <= nums[index] and left<right:
            while (not self.large(nums[left] , nums[index])) and left<right:
                left = left +1
            #print "find left > index ,left=", left
            
            if left < right:
                #print "swap nums[left],nums[right]",left, right
                nums[left],nums[right]=nums[right],nums[left]
                
        #print "swap nums[left],nums[right]",left,index
        nums[left],nums[index]=nums[index],nums[left]
        #print  "index = ", index ," left - 1=", left - 1 , " left + 1=", left + 1, " end=", end
        self.quickSort(nums,index,left-1)
        self.quickSort(nums,left+1,end)

    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        self.quickSort(nums,0,len(nums)-1)
        retStr=""
        i=len(nums)-1
        while i>=0:
            retStr=retStr + str(nums[i])
            i=i-1
        return retStr


sol=Solution()


#print sol.largestNumber([3,30,34,5,9])
#a=[3,30,34,5,9]
#sol.quick_sort(a,0,4)
#print "========================"
#a=[3,30,34,5,9]
#sol.quickSort(a,0,4)
a=[3,30,34,5,9,2,123]
a=[3,30,34,5,9]
print sol.largestNumber(a)

#print sol.large(301,34)
#print sol.large(9,3)
#print sol.large(9,30)
#print sol.large(3,30)