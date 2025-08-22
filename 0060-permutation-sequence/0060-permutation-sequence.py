class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = []
        for i in range(1,n+1):
            arr.append(i)
        
        res = [] 
        sol = []
        def backtrack():
            if len(res)==k:
                return 
            if len(sol) == len(arr):
                res.append(sol[:])
                return 
            for num in arr:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()
        backtrack()

        ans = ""
        for elem in res[k-1]:
            ans+=str(elem)
        return ans
        