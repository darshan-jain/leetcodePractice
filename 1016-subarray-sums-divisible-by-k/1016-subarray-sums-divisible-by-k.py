class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0 
        res = 0 
        prefix_count = defaultdict(int)
        prefix_count[0]=1

        for num in nums:
            prefix_sum+=num
            remain = prefix_sum%k
            res+=prefix_count[remain]
            prefix_count[remain]+=1
        return res