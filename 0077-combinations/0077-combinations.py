class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(i,sol ):
            if len(sol)==k:
                res.append(sol[:])
                return 
            for j in range(i+1, n+1):
                if j not in sol:
                    sol.append(j)
                    backtrack(j, sol)
                    sol.pop()


        for i in range(1,n+1):
            backtrack(i,[i])
        return res
        