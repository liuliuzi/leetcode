class Solution(object):
    def getMinimumDifference(self, root):        
        def inorder(root):
            if not root: return
            inorder(root.left)
            if self.prev is not None: 
                self.minDiff = min(self.minDiff, root.val - self.prev)
            self.prev = root.val
            inorder(root.right)
        
        self.prev = None
        self.minDiff = float('inf')
        inorder(root)
        return self.minDiff