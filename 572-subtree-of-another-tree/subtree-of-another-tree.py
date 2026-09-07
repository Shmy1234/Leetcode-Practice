# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def same(r, s):
            if not s and not r:
                return True
            elif s and r and s.val == r.val:
                return same(r.left, s.left) and same(r.right, s.right)
        
        if not root: 
            return False
        elif not subRoot: 
            return True
        elif same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        
