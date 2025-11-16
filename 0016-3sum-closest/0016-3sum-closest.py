class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest  = float("inf")
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            lo,hi = i +1, len(nums)-1
            while lo<hi:
                tot = nums[i] + nums[lo] + nums[hi]
                if abs(tot-target) < abs(closest-target):
                    closest = tot 
                if tot ==target:
                    return tot 
                elif tot > target:
                    hi-=1
                else:
                    lo+=1
        return closest
        