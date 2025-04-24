class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def combination(part,start,target):
            if target==0:
                res.append(part)
                return 
            for i in range(start, len(candidates)):
                if candidates[i]>target:
                    continue
                combination(part + [candidates[i]], i, target - candidates[i])


        combination([],0,target)
        return res
        