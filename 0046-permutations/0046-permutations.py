class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack():
            if len(sol)==len(nums):
                res.append(sol[:]) # remember to store a copy of sol since while backtracking sol will again be []
                return 
            for num in nums:
                if num not in sol:   #this will make sure that the previous elements doesn't repeat while traversing the loop structure
                    sol.append(num)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return res
        