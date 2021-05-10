# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:        # IF the current node is null
            return "X#"     # X represents NULL and # is separator
        
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        
        return str(root.val)+"#"+left+right
        
    def dfs(self, data):
        """Iterates through the encoded data queue"""
        val = next(data)
        if(val == "X"):
            return None
        node = TreeNode(int(val))

        node.left = self.dfs(data)
        node.right = self.dfs(data)
        
        return node
            
    
    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        
        data_list = iter(data.split("#"))
        return self.dfs(data_list)
        
            

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans