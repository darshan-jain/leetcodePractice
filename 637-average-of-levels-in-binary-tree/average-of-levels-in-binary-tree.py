# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return []

        next_level = []
        answer = []
        curr = root
        present_level = [curr]
        while present_level != []:
            for curr in present_level:
                valu = 0 
                if curr.left is not None:
                    next_level.append(curr.left)
                if curr.right is not None:
                    next_level.append(curr.right)
                for item in present_level:
                    valu += item.val
                ans = valu / len(present_level)
            answer.append(ans)
            present_level = next_level
            next_level = []
            
        return answer
            
        