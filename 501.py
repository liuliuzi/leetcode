
import collections
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        count = collections.defaultdict(int)
        def preorder(root):
            if root:

                count[root.val] += 1
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        max_occ = max(count.values())
        return [k for k in count if count[k] == max_occ]
