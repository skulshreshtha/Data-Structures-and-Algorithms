# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        
        if not root:
            return ans
        
        q = deque()
        
        q.append(root)                  # Add root node to queue
        count = 1
        
        while q:
            temp = []
            added = 0
            for i in range(count):
                el = q.popleft()
                if el.left:
                    q.append(el.left)
                    added += 1
                if el.right:
                    q.append(el.right)
                    added += 1
                temp.append(el.val)
            ans.append(temp)
            count = added
            
        return ans
            