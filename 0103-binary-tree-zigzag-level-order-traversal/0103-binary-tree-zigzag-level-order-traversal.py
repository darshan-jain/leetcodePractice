# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        turn = 0 
        curr_level = [root]
        res = []
        while curr_level:
            next_level = []
            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            path = []
            for item in curr_level:
                path.append(item.val)
            if(turn%2==0):
                res.append(path)
            else:
                res.append(path[::-1])
            turn+=1
            curr_level = next_level
        return res

        