class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res = 0 
        def getlast(val):
            
            l = 0 
            r = len(nums)-1
            ans = -1
            while l<=r:
                m = (l+r)//2
                if nums[m]==val:
                    ans = max(ans,m)
                    l = m+1
                elif nums[m] > val:
                    r = m-1
                else:
                    l = m+1
            return ans
        for i,num in enumerate(nums):
            if i>0 and nums[i]==nums[i-1]:
                continue
           
            lastindex = getlast(num+1)
            if lastindex!=-1:
                print(i,lastindex)
                res = max(res,lastindex-i+1 )
        return res

        