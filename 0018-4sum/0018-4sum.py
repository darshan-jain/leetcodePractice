class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        hm = defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                hm[nums[i] + nums[j]].append((i,j))
        
        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                tofind = target - nums[i]-nums[j]
                if tofind in hm:
                    vals = hm[tofind]
                    for k,l in vals:
                        if k>j:
                            if len(res)!=0 and nums[i]==res[-1][0] and nums[j]==res[-1][1] and nums[k]==res[-1][2] and nums[l]==res[-1][3]:
                                continue
                            res.append([nums[i], nums[j], nums[k], nums[l]])
        
        return res


        