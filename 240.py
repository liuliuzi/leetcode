class Array:
    def __init__(self, lst):
        self.__coll = lst

    def __repr__(self):
        return '{!r}'.format(self.__coll)
    
    def __len__(self):
        return len(self.__coll)
    
    def volNumber(self):
        return len(self.__coll[0])

    def __getitem__(self, key):    
            slice1, slice2 = key
            if isinstance(slice1,slice):
                row1 = slice1.start if slice1.start!=None else 0
                row2 = slice1.stop if slice1.stop!=None else len(self.__coll)
            elif isinstance(slice1,int):
                row1=row2=slice1
            else:
                raise NotImplementedError
            
            if isinstance(slice2,slice):
                col1 = slice2.start if slice2.start!=None else 0
                col2 = slice2.stop if slice2.stop!=None else len(self.__coll[0])
            elif isinstance(slice2,int):
                col1=col2=slice2
            else:
                raise NotImplementedError
                
            if row1==row2 and col1==col2: 
                if (isinstance(slice1,slice) or isinstance(slice2,slice)):
                    return [[self.__coll[row1][col1]]]
                else:
                    return self.__coll[row1][col1]
            else:
                return [self.__coll[r][col1:col2] for r in range(row1, row2)]

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix[0])==0:
            return False

        if not isinstance(matrix,Array):
            matrix=Array(matrix)
        if target < matrix[0,0] or target > matrix[-1,-1]:
            return False

        if len(matrix)==1 and matrix.volNumber()==1:
            if matrix[0,0]==target:
                return True
            else:
                return False
        else:
            crossRow=len(matrix)/2-1 if len(matrix)/2-1 >0 else 0
            crossVol=(matrix.volNumber())/2-1  if (matrix.volNumber())/2-1 >0 else 0
            if matrix[crossRow,crossVol]>=target:
                return self.searchMatrix(matrix[0:crossRow,0:crossVol],target)
            else:
                righttop = matrix[0:crossRow+1,crossVol+1:]
                leftebutton = matrix[crossRow+1:,0:crossVol+1]
                rightbutton = matrix[crossRow+1:,crossVol+1:]
                righttopRet=leftebuttonRet=rightbuttonRet=False
                if len(righttop)!=0:
                    righttopRet = self.searchMatrix(righttop,target)
                if len(leftebutton)!=0:
                    leftebuttonRet = self.searchMatrix(leftebutton,target)
                if len(rightbutton)!=0:
                    rightbuttonRet = self.searchMatrix(rightbutton,target)

                
                return righttopRet or leftebuttonRet or rightbuttonRet
        
sol=Solution()
aa=[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print sol.searchMatrix(aa,18)
print sol.searchMatrix(aa,1)
print sol.searchMatrix(aa,6)
print sol.searchMatrix(aa,11)
print sol.searchMatrix(aa,23)
print sol.searchMatrix(aa,20)
