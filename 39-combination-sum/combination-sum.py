class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def comb(curr,start,target):
            if target == 0 :
                res.append(curr)
                return 
            for i in range(start, len(candidates)):
                if candidates[i]>target:
                    continue
                comb(curr + [candidates[i]], i, target - candidates[i])
    
        comb([],0,target)
        return res
        