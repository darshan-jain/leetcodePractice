class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num <0:
                neg.append(num)
            else:
                pos.append(num)
        res = []
        i = 0 
        j = 0 
        while i<len(pos) and j<len(neg):
            res.append(pos[i])
            res.append(neg[i])
            i+=1
            j+=1
        return res
        