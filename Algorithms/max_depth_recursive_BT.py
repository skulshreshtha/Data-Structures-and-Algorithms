# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _recursive_depth(self, t: TreeNode, d: int) -> int:
        
        if not t:
            return d
        if(t.left is None and t.right is None):
            return d
        
        d_l = self._recursive_depth(t.left, d+1)
        d_r = self._recursive_depth(t.right, d+1)
        
        return max(d, d_l, d_r)
        
        
    
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        return self._recursive_depth(root,1)