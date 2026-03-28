class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def comb(path, start, target):
            if target==0:
                res.append(path[:])
                return 
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                comb(path + [candidates[i]], i+1, target-candidates[i])
        
        comb([],0,target)
        return res
        