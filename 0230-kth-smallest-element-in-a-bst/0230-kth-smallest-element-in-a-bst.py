# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        In-order traversal will created sorted list. If I stop traversal at k
        """
        sorted_vals = []
        def dfs(node):
            nonlocal sorted_vals
            if not node: 
                return
            # In order traversal with recursive calls
            dfs(node.left)
            if len(sorted_vals) < k:
                sorted_vals.append(node.val)
            dfs(node.right)
        dfs(root)
        return sorted_vals[-1]


