class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        minn = min(p.val, q.val)
        maxn = max(p.val, q.val)
        if root is None:
            return None
        if minn <= root.val <= maxn:
            return root
        else:
            l = lowestCommonAncestor(root.left, p, q)
            r = lowestCommonAncestor(root.right, p, q)
            if l:
                return l
            if r:
                return r