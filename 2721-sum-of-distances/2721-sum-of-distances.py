class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hm = defaultdict(list)
        for i, num in enumerate(nums):
            hm[num].append(i)
        res = [0]*n
        for k,lst in hm.items():
            if len(lst)>1:
                m = len(lst)
                total = sum(lst)
                prefix = 0 
                for i,idx in enumerate(lst):
                    leftsum = i*idx - prefix 
                    suffix = total - prefix - idx 
                    rightsum = suffix - (m-1-i)*idx
                    prefix+=idx
                    res[idx] = leftsum+rightsum
            else:
                res[lst[0]]=0
        return res
        