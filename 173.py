# Definition for a  binary tree node
class TreeNode(object):
     def __init__(self, x ,left, right):
         self.val = x
         self.left = left
         self.right = right

class BSTIterator(object):
    def __init__(self, root):
        self.minval = 0
        self.L = []
        while root is not None:
            self.L.append(root)
            root = root.left

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.L) == 0:
            return False
        else:
            curNode = self.L.pop()
            self.minval = curNode.val
            
            if curNode.right is not None:
                newNode = curNode.right
                while newNode is not None:
                    self.L.append(newNode)
                    newNode = newNode.left
            
            return True

    # @return an integer, the next smallest number
    def next(self):
        return self.minval
        

# Your BSTIterator will be called like this:
root = TreeNode(8,TreeNode(3,TreeNode(1,None,None),TreeNode(6,TreeNode(4,None,None),TreeNode(7,None,None))),TreeNode(10,None,TreeNode(14,TreeNode(13,None,None),None)))
#root = TreeNode(8,TreeNode(3,None,None),TreeNode(10,None,None))



i, v = BSTIterator(root), []
while i.hasNext(): v.append(i.next())
print v
