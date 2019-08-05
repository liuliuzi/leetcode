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

        lenth=len(maze[0])
        height=len(maze)

        retArr=[]
        
        def roll(maze, start, destination):
            hasRoad=False
            maze[start[0]][start[1]]=3 

            if start[0]+1<lenth and maze[start[0]+1][start[1]]!=1 : #down
                i=start[0]+1
                while i+1 <lenth and maze[i+1][start[1]]!=1:
                    if onDestination(i,start[1],destination): #onDestination
                        retArr.append("d")
                        return True
                    i=i+1
                if maze[i][start[1]]!=3:
                    #hasRoad=True
                    #maze[i][start[1]]=3
                    print "v",[start[0],start[1]], "to" ,[i,start[1]]
                    retArr.append("d")
                    if roll(maze, [i,start[1]], destination):
                        return True
            
            if start[1]-1>=0 and maze[start[0]][start[1]-1]!=1 : #left
                i=start[1]-1
                while i-1 >=0 and maze[start[0]][i-1]!=1:
                    if onDestination(start[0],i,destination): #onDestination
                        retArr.append("l")
                        return True
                    i=i-1
                if maze[start[0]][i]!=3:
                    #hasRoad=True
                    #maze[start[1]][i]=3
                    print "<-", [start[0],start[1]], "to" , [start[0],i]
                    retArr.append("l")
                    if roll(maze, [start[0],i], destination):
                        return True

            if start[1]+1<height and maze[start[0]][start[1]+1]!=1 : #right
                i=start[1]+1
                while i+1 <height and maze[start[0]][i+1]!=1:
                    if onDestination(start[0],i,destination): #onDestination
                        retArr.append("r")
                        return True
                    i=i+1
                if maze[start[0]][i]!=3: #had cap 
                    print "->", [start[0],start[1]], "to" , [start[0],i]
                    retArr.append("r")
                    if roll(maze, [start[0],i], destination):
                        return True

            if start[0]-1>=0 and maze[start[0]-1][start[1]]!=1 : #up
                i=start[0]-1
                while i-1 >=0 and maze[i-1][start[1]]!=1:
                    if onDestination(i,start[1],destination): #onDestination
                        retArr.append("u")
                        return True
                    i=i-1
                if maze[i][start[1]]!=3:
                    #hasRoad=True
                    #maze[i][start[1]]=3
                    print "^",[start[0],start[1]], "to" , [i,start[1]]
                    retArr.append("u")
                    if roll(maze, [i,start[1]], destination):
                        return True


            if len(retArr)>0:
                retArr.pop()
            return False


        hasRoad=roll(maze, start, destination)
        if hasRoad:
            return str(retArr)
        else:
            return "impossble"

sol=Solution()
maze=[[0, 0, 0, 0, 0],
[1, 1, 0, 0, 1],
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 1, 0, 0, 0]]
start=[4,3]
destination=[0,1]


print sol.hasPath(maze, start, destination)


