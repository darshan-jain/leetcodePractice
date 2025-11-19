# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def __init__(self):
        self.hm = {}
    def relationship(self,curr,parent):
        if curr is None:
            return 
        self.hm[curr] = parent
        self.relationship(curr.left,curr)
        self.relationship(curr.right, curr)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #edge case 
        if root is None:
            return []
        #build a hashmap of child -> parent
        self.relationship(root, None)

        #using a Queue -> Do BFS 
        q = deque([target])
        visit = set()
        res = []
        while q and k>0:
            k-=1
            for i in range(len(q)):
                curr = q.popleft()
                visit.add(curr)
                if curr.left and curr.left not in visit:
                    q.append(curr.left)
                if curr.right and curr.right not in visit:
                    q.append(curr.right)
                if self.hm[curr] and self.hm[curr] not in visit:
                    q.append(self.hm[curr])
        
        while q:
            curr = q.popleft()
            res.append(curr.val)
        return res








        