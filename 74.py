class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        row=0
        m=len(matrix)
        n=len(matrix[0])
        
        if target>=matrix[m-1][0]:
            row=m-1
        else:
            for i in range(len(matrix)):
                if target<matrix[i][0]:
                    row=i-1
                    break             
        if row<0:
            return False
            
        j=0

        '''
        while j<n:
            if matrix[row][j]==target:
                return True
            elif matrix[row][j]>target:
                return False
            else:
                j+=1
        '''
        def twoFind(left,right,target):            
            if matrix[row][left] == target or matrix[row][right] == target:
                return True
            if left==right:
                return False

            mid=(left+right)/2
            if target==matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                return twoFind(left+1,mid,target)
            else:
                return twoFind(mid,right-1,target)

                
        return twoFind(0,n-1,target)


matrix=[[1,   3,  5,  7],  [10, 11, 16, 20],  [23, 30, 34, 50]]
sol=Solution()
print  sol.searchMatrix(matrix,7)
print  sol.searchMatrix(matrix,10)
print  sol.searchMatrix(matrix,16)
print  sol.searchMatrix(matrix,12)
