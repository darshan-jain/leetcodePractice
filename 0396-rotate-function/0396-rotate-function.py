class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        nums += nums
        res = float("-inf")
        ans = 0 
        val=0
        for i in range(n):
            ans+=(i*nums[i])
            val+=nums[i]
        val -= nums[0]
        res = max(res, ans)
        print(ans, val)
        for i in range(1, n):
            ans = ans - val + (n-1)*nums[i + n-1]
            val += nums[i+n-1]
            val-=nums[i]
            res = max(ans,res)
            print(ans,res)
        return res




        