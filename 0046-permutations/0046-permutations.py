class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def perm(sol):
            if len(sol)==len(nums):
                res.append(sol[:])
                return 
            for num in nums:
                if num not in sol:
                    sol.append(num)
                    perm(sol)
                    sol.pop()
        
        perm([])
        return res
        