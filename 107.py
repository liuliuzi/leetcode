# Definition for a binary tree node.

class TreeNode(object):
     def __init__(self, x,y,z):
         self.val = x
         self.left = y
         self.right = z

class Solution(object):
    def __init__(self):
        self.list=[]
        self.map={}
    def insertMap(self, x, level):
    	if self.map.has_key(level):
    		self.map[level].append(x)
    	else:
    		self.map[level]=[x]

    def map2List(self):
    	keys = self.map.keys()
    	keys.sort(reverse=True)
    	return map(self.map.get,keys)

    def levelOrder(self, root):
    	self.change(root,0)
    	#print 1,self.map
    	return self.map2List()

    def change(self, root,level):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if level== None:
        	level=0
        if root.val == None:
        	return
        if root.left != None:
        	self.change(root.left,level+1)
        self.insertMap(root.val,level)
        if root.right != None:
        	self.change(root.right,level+1)


sol=Solution()
n = TreeNode(2,TreeNode(6,TreeNode(2,None,None),TreeNode(4,None,None)),TreeNode(7,TreeNode(9,None,None),TreeNode(8,None,None)))
print n
sol.levelOrder(n)
#print sol.twoSum([3, 2, 4],6)