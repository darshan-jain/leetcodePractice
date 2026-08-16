class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sol = []
        count = Counter(nums)

        def dfs():
            if len(sol)==len(nums):
                ans.append(sol[:])
                return 
            for num in count:
                if count[num]>0:
                    sol.append(num)
                    count[num]-=1
                    dfs()
                    sol.pop()
                    count[num]+=1


        dfs()
        return ans
        