class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums)<4:
            return []
        ans = []
        nums.sort()
        hm = defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                val = nums[i]+ nums[j]
                hm[val].append([i,j])
        #print(hm)

        for i in range(len(nums)-1):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                valtofind = target - nums[i] - nums[j]
                if valtofind in hm:
                    lst = hm[valtofind]
                    for k,l in lst:
                        if k>j:
                            if len(ans)!=0 and ans[-1][0]==nums[i] and ans[-1][1]==nums[j] and ans[-1][2]==nums[k] and ans[-1][3]==nums[l]:
                                continue
                            ans.append([nums[i], nums[j], nums[k], nums[l]])


        return ans



        