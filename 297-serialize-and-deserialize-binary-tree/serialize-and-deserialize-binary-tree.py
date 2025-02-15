# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import ast
class Codec:

    def helper(self,node,lst):
        if node is None:
            lst.append("null")
            return 
        lst.append(str(node.val))
        self.helper(node.left,lst)
        self.helper(node.right,lst)

        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        lst = []
        self.helper(root, lst)
        return str(lst)
        
    def helper2(self,data):
        val = data.pop()
        if val == "null":
            return None
        node = TreeNode(int(val))
        node.left = self.helper2(data)
        node.right = self.helper2(data)
        return node
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = ast.literal_eval(data)
        data.reverse()
        print(data)
        node = self.helper2(data)
        return node

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))