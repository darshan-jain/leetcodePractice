class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = collections.defaultdict(list)
        for i in range(len(nums)):
            hm[nums[i]].append(i)
        for key,lst in hm.items():
            for i,j in pairwise(lst):
                if abs(i-j)<=k:
                    return True
        return False
        