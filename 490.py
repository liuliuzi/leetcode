'''
Input 1: a maze represented by a 2D array
0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0
Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)
Output: true
'''
import copy
class Solution(object):
    
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        def onDestination(i,j,destination):
            if i==destination[0] and j==destination[1]:
                return True
            return False

        if onDestination(start[0],start[1],destination):
            return True     
        if maze[start[0]][start[1]]==1:
            return False
        lenth=len(maze[0])
        height=len(maze)
        
        def roll(maze, start, destination):
            hasRoad=False
            maze[start[0]][start[1]]=3        
            if start[0]-1>=0 and maze[start[0]-1][start[1]]!=1 : #up
                i=start[0]-1
                while i-1 >=0 and maze[i-1][start[1]]!=1:
                    i=i-1

                if onDestination(i,start[1],destination): #onDestination
                    return True
                if maze[i][start[1]]!=3:
                    #hasRoad=True
                    #maze[i][start[1]]=3
                    print "^",[start[0],start[1]], "to" , [i,start[1]]
                    hasRoad=hasRoad or roll(maze, [i,start[1]], destination)

            if start[0]+1<lenth and maze[start[0]+1][start[1]]!=1 : #down
                i=start[0]+1
                while i+1 <lenth and maze[i+1][start[1]]!=1:
                    i=i+1

                if onDestination(i,start[1],destination): #onDestination
                    return True
                if maze[i][start[1]]!=3:
                    #hasRoad=True
                    #maze[i][start[1]]=3
                    print "v",[start[0],start[1]], "to" ,[i,start[1]]
                    hasRoad=hasRoad or roll(maze, [i,start[1]], destination)
            
            if start[1]-1>=0 and maze[start[0]][start[1]-1]!=1 : #left
                i=start[1]-1
                while i-1 >=0 and maze[start[0]][i-1]!=1:
                    i=i-1

                if onDestination(start[0],i,destination): #onDestination
                    return True
                if maze[start[0]][i]!=3:
                    #hasRoad=True
                    #maze[start[1]][i]=3
                    print "<-", [start[0],start[1]], "to" , [start[0],i]
                    hasRoad=hasRoad or roll(maze, [start[0],i], destination)
            
            if start[1]+1<height and maze[start[0]][start[1]+1]!=1 : #right
                i=start[1]+1
                while i+1 <height and maze[start[0]][i+1]!=1:
                    i=i+1

                if onDestination(start[0],i,destination): #onDestination
                    return True
                if maze[start[0]][i]!=3: #had cap 
                    print "->", [start[0],start[1]], "to" , [start[0],i]
                    hasRoad=hasRoad or roll(maze, [start[0],i], destination)

            if hasRoad==False:
                return False
            return True

        return roll(maze, start, destination)

sol=Solution()
maze=[[0, 0, 1, 0, 0],
      [0, 0, 0, 0, 0],
      [0, 0, 0, 1, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 0, 0, 0]]
start=[0,4]
destination=[4,4]
maze2=copy.copy(maze)
start2=[0,4]
destination2=[3,2]

#print sol.hasPath(maze, start, destination)
print sol.hasPath(maze2, start2, destination2)

