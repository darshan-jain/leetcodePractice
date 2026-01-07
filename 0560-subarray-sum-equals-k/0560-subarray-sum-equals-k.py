class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hm = defaultdict(int)
        hm[0] = 1
        res = 0 
        curSum = 0 
        diff = 0 
        for num in nums:
            curSum+=num
            diff = curSum-k
            if diff in hm:
                res+=hm[diff]
            hm[curSum]+=1
        return res
        