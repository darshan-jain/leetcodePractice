class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def comb(path, start, target):
            if target==0:
                res.append(path[:])
                return 
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    continue
                comb(path + [candidates[i]], i, target - candidates[i])
        comb([], 0 , target)
        return res
        