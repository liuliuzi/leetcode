class Solution(object):
    #valMap={}
    def __init__(self):
      self.valMap={}
    def cachminFun(self,x,y,value):
      if self.valMap.has_key(x):
        if not self.valMap.has_key(y):
          print x,y,"add x y cached x"
          self.valMap[x][y]=self.minFun(x,y,triangle)
      else:
        self.valMap[x]={}
        print x,y,"add x y cached 0"
        self.valMap[x][y]=self.minFun(x,y,triangle)

      return self.valMap[x][y]

    def minFun(self, x,y,triangle):
        if x==0 and y==0:
          return triangle[0][0]
        elif x==1:
          return triangle[0][0]+triangle[1][y]
        elif y==0:
          return self.minFun(x-1,y,triangle)+triangle[x][y]
        elif y==x:
          return self.minFun(x-1,y-1,triangle)+triangle[x][y]
        else:
          xx=min(self.minFun(x-1,y-1,triangle),self.minFun(x-1,y,triangle))
          return xx + triangle[x][y]
          #return min(self.minFun(x-1,y-1,triangle),self.minFun(x-1,y,triangle))+triangle[x][y]

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        #f(x,y)=min(f(x-1,y-1)f(x-1,y)+t[x,y]
        #f(0,0)=t[0,0]

        n = len(triangle)
        dp = [0] * n
        for i in range(n-1,-1,-1):
          dp[i]=self.cachminFun(n-1,i,triangle)

        print dp
        return min(dp)

class Solution2(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)

        dp = triangle[n-1]

        for i in range(n-2,-1,-1):
            for j in range(i+1):
                dp[j] = min( dp[j], dp[j+1] ) + triangle[i][j]
        return dp[0]

sol1=Solution()
sol2=Solution2()
triangle=[
[2],
[3,4],
[6,5,7],
[4,1,8,3],
[4,2,5,9,2]
]
#print sol.minimumTotal2(triangle)
print triangle
print sol1.minimumTotal(triangle)
print triangle
print sol2.minimumTotal(triangle)
