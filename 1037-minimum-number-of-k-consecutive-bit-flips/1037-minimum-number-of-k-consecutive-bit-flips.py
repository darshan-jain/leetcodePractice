class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = 0 
        times = 0 
        flip = [0]*n
        for i in range(n):
            if i>=k:
                times-=flip[i-k]
            
            if (nums[i]==1 and times%2==1) or (nums[i]==0 and times%2==0):
                if i+k>n:
                    return -1
                ans+=1
                times+=1
                flip[i]=1
        return ans
        