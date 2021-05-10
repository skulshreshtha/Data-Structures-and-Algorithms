# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def _LCA(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        if not node:
            return None
        if(node.val == p.val or node.val == q.val):
            return node
        
        left = self._LCA(node.left, p, q)
        right = self._LCA(node.right, p, q)
        
        if(left is None and right is None):
            return None
        if(left and right):
            return node
        if(left):
            return left
        return right
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self._LCA(root, p, q)