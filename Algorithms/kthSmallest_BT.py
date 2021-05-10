# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def _inorder(self, node: TreeNode):
        
        temp = []
        if node:
            temp += self._inorder(node.left)
            temp += [node.val]
            temp += self._inorder(node.right)
        
        return temp
            
            
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        inorder = self._inorder(root)
        return inorder[k-1]