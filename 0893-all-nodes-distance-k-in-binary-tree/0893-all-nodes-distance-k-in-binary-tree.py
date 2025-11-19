# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    def __init__(self):
        self.hm = {}
    def relationship(self,curr,parent):
        if not curr:
            return 
        self.hm[curr] = parent
        self.relationship(curr.left, curr)
        self.relationship(curr.right, curr)
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        #edge case 
        if not root:
            return []
        
        #build the hashmap 
        self.relationship(root, None)

        #BFS
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
            node = q.popleft()
            res.append(node.val)
        return res


        