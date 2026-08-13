class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0 
        hm = {}
        for num in nums:
            if num in hm:
                ans+=hm[num]
                hm[num]+=1
            else:
                hm[num]=1
        return ans

        