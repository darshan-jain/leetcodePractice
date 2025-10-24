class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i,num in enumerate(nums):
            if target-num in hm:
                return [i,hm[target-num]]
            hm[num]=i
        return [0,1]
        