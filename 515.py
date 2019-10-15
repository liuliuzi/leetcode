'''
Input: 
          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
'''
# Definition for a binary tree node.
import collections
class TreeNode(object):
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def largestValuesByBFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = collections.deque()
        res = []
        queue.append(root)
        while queue:
            size = len(queue)
            if queue[0]==None:
                break
            max_level = queue[0].val
            for i in range(size):
                node = queue.popleft()
                if not node: continue
                max_level = max(max_level, node.val)
                queue.append(node.left)
                queue.append(node.right)
            res.append(max_level)
        return res

    def largestValuesByDFS(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        nodeList=[]
        level = 0
        def findNodeVal(root,level):      
            if root != None:
                if level >= len(nodeList):
                    nodeList.append([root.val])
                else:
                    nodeList[level].append(root.val)
                findNodeVal(root.left,level+1)
                findNodeVal(root.right,level+1)
        findNodeVal(root,level)
        print(nodeList)

        for key in range(len(nodeList)):
            res.append(max(nodeList[key]))
        return res
sol=Solution()
tree=TreeNode(1,TreeNode(3,TreeNode(5),TreeNode(3)),TreeNode(2,None,TreeNode(9)))
print(sol.largestValuesByDFS(tree))
print(sol.largestValuesByBFS(tree))
