'''
Input:
11110
11010
11000
00000

Output: 1
'''
class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands=0
        row=len(grid)
        vol=len(grid[0])

        def expent(x,y):
            if x>=0 and y>=0 and x<row and y <vol:
                if x==4 and y==3:
                    pass
                if grid[x][y]!=0:
                    grid[x][y]=0
                    expent(x-1,y)
                    expent(x+1,y)
                    expent(x,y-1)
                    expent(x,y+1)


        for x in range(row):
            for y in range(vol):
                if grid[x][y]==1:
                    islands=islands+1
                    expent(x,y)
        return islands
                    
sol=Solution()
print sol.numIslands(
[[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]])

print sol.numIslands(
[[1,1,0,0,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,1]])

print sol.numIslands(
[[1,1,1,1,1],
[1,1,0,0,1],
[1,1,0,1,1],
[0,0,1,1,0]])