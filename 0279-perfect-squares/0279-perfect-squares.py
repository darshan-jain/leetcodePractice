class Solution:
    def numSquares(self, n: int) -> int:
        maxval = n//2
        nums = []
        for i in range(1,maxval+1):
            if i**2 <=n:
                nums.append(i**2)
        
        print(nums)

        if len(nums)==0:
            return n

        target=n
        dp = [target+1]*(target+1)
        dp[0]=0
        for i in range(1,target+1):
            for num in nums:
                if i>=num and dp[i-num]!=target+1:
                    dp[i]= min(dp[i], 1+dp[i-num])
        print(dp)
        return dp[-1]


        