class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.sum = 0
        self.inOrder(root)
        return self.sum

    def inOrder(self, root):
        if not root: return 
        if root.left:
            self.inOrder(root.left)
            if not root.left.left and not root.left.right:
                self.sum += root.left.val
        if root.right:
            self.inOrder(root.right)
