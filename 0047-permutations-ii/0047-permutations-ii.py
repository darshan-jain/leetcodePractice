class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sol = []
        count = Counter(nums)

        def dfs():
            if len(sol)==len(nums):
                ans.append(sol[:])
                return 
            for n in count:
                if count[n]>0:
                    sol.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    sol.pop()
        
        dfs()
        return ans
        