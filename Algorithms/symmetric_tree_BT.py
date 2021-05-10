# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _isMirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if(t1 is None and t2 is None):
            return True
        if(t1 is None or t2 is None):
            return False
        
        return (t1.val == t2.val and self._isMirror(t1.left,t2.right) and self._isMirror(t1.right,t2.left))
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self._isMirror(root,root)