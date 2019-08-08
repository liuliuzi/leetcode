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
        
        if onDestination(start[0],start[1],destination):
            return 0


        lenth=len(maze[0])
        height=len(maze)
        for x in range(height):
            for y in range(lenth):
                if maze[x][y]==1:
                    maze[x][y]=-1

        retArr=[]
        
        
        def roll(maze, start, destination,steps):
            #hasRoad=False
            #maze[start[0]][start[1]]=3 

            if start[0]+1<lenth and maze[start[0]+1][start[1]]!=-1 : #down
                i=start[0]+1
                while i+1 <lenth and maze[i+1][start[1]]!=-1:
                    if onDestination(i,start[1],destination): #onDestination
                        return steps+i-start[0]
                    i=i+1
                if maze[i][start[1]]==0 or maze[i][start[1]]>steps+i-start[0]:
                    #hasRoad=True
                    maze[i][start[1]]=steps+i-start[0]
                    print "v",[start[0],start[1]], "to" ,[i,start[1]]
                    newstep = roll(maze, [i,start[1]], destination, steps+i-start[0])
                    if newstep:
                        return newstep
            
            if start[1]-1>=0 and maze[start[0]][start[1]-1]!=-1 : #left
                i=start[1]-1
                while i-1 >=0 and maze[start[0]][i-1]!=-1:
                    if onDestination(start[0],i,destination): #onDestination
                        return steps-i+start[1]
                    i=i-1
                if maze[start[0]][i]==0 or maze[start[0]][i]>steps-i+start[1]:
                    #hasRoad=True
                    maze[start[0]][i]=steps-i+start[1]
                    print "<-", [start[0],start[1]], "to" , [start[0],i]
                    newstep =roll(maze, [start[0],i], destination, steps-i+start[1])
                    if newstep:
                        return newstep

            if start[1]+1<height and maze[start[0]][start[1]+1]!=-1 : #right
                i=start[1]+1
                while i+1 <height and maze[start[0]][i+1]!=-1:
                    if onDestination(start[0],i,destination): #onDestination
                        return steps+i-start[1]
                    i=i+1
                if maze[start[0]][i]==0 or maze[start[0]][i]>steps+i-start[1]:
                    maze[start[0]][i]=steps+i-start[1]
                    print "->", [start[0],start[1]], "to" , [start[0],i]
                    newstep = roll(maze, [start[0],i], destination, steps+i-start[1])
                    if newstep:
                        return newstep

            if start[0]-1>=0 and maze[start[0]-1][start[1]]!=-1 : #up
                i=start[0]-1
                while i-1 >=0 and maze[i-1][start[1]]!=-1:
                    if onDestination(i,start[1],destination): #onDestination
                        return steps-i+start[0]
                    i=i-1
                if maze[i][start[1]]==0 or maze[i][start[1]]>steps-i+start[0]:
                    #hasRoad=True
                    maze[i][start[1]]=steps-i+start[0]
                    print "^",[start[0],start[1]], "to" , [i,start[1]]
                    newstep =roll(maze, [i,start[1]], destination, steps-i+start[0])
                    if newstep:
                        return newstep

        #steps = roll(maze, start, destination, 0)
        stepsArry=[]

        while True:
            newsteps = roll(maze, start, destination, 0)
            print "*"*20
            if newsteps !=None:
                stepsArry.append(newsteps)
            else:
                break
        return min(stepsArry)

sol=Solution()
maze=[
[0, 0, 0, 0, 0],
[1, 1, 0, 0, 1],
[0, 0, 0, 0, 0],
[0, 1, 0, 0, 1],
[0, 1, 0, 0, 0]]
start=[4,3]
destination=[0,1]


print sol.hasPath(maze, start, destination)


