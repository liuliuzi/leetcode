'''Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
'''
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        q = collections.deque()
        q.append(root)
        res = []
        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                if not node: continue
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if level:
                res.append(level)
        return res[-1][0]


