class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        cache = {}

        def dfs(i):
            if i>=len(arr):
                return 0 
            if i in cache:
                return cache[i]
            res = 0 
            currmax = 0 
            for j in range(i, min(len(arr),i+k)):
                currmax = max(currmax, arr[j])
                winsize = j-i+1
                res = max(res, dfs(j+1)+ currmax*winsize)
                cache[i] = res
            return res

        return dfs(0)
        