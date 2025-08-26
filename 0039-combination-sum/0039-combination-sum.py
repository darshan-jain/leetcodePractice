class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def comb(start, part, target):
            if target==0:
                res.append(part[:])
                return 
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                comb(i, part + [candidates[i]], target - candidates[i])
        

        comb(0,[],target)
        return res
        