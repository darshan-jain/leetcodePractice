class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        hm = defaultdict(list)
        n = len(arr)
        for i,num in enumerate(arr):
            hm[num].append(i)
        res = [0]*n
        for k,lst in hm.items():
            m = len(lst)
            if m<=1:
                res[lst[0]]=0
                continue
            else:
                prefix = 0 
                total = sum(lst)
                for i,idx in enumerate(lst):
                    leftsum = i*idx - prefix
                    suffix = total - prefix - idx 
                    rightsum = suffix - (m-1-i)*idx 
                    prefix+=idx 
                    res[idx] = leftsum + rightsum 
        return res

        