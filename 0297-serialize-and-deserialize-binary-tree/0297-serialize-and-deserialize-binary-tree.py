# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import ast
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(root):
            if root is None:
                return ["null"]
            return [str(root.val)] + dfs(root.left) + dfs(root.right)
        val = dfs(root)
        return str(val)
    
    def helper(self,data):
        val = data.pop()
        if val=="null":
            return None
        node = TreeNode(val)
        node.left = self.helper(data)
        node.right = self.helper(data)
        return node

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = ast.literal_eval(data) #safely evals the string
        data = data[::-1]
        node = self.helper(data)
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))