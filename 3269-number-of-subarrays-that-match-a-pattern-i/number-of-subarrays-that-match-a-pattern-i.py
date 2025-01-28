class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        ans = 0 
        n = len(nums)
        m = len(pattern)

        for i in range(0,n-m):
            flag = 0 
            for k in range(0,m):
                if (pattern[k]==1 and nums[i+k+1] > nums[i+k]) or (pattern[k]==0 and nums[i+k+1] == nums[i+k]) or (pattern[k]==-1 and nums[i+k+1] < nums[i+k]):
                    continue
                else:
                    flag = 1
                    break
            if flag == 0 :
                ans+=1
        return ans
        