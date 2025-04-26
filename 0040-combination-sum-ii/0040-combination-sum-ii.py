class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(path, index, target):
            if target ==0:
                res.append(path[:])
                return 
            
            for j in range(index,len(candidates)):
                if candidates[j]>target:
                    break
                if j > index and candidates[j]==candidates[j-1]:
                    continue
                backtrack(path+[candidates[j]], j+1, target - candidates[j])
        
        backtrack([],0,target)
        return res
        