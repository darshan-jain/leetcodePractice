class Solution:
    def __init__(self):
        self.ans = []
    def helper(self,p,up):
        if len(up)==0:
            self.ans.append(p)
            return 
        self.helper(p+[up[0]], up[1:])
        self.helper(p, up[1:])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.helper([],nums)
        return self.ans
        