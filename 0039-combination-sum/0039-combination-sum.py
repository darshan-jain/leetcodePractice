class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def comb(path,i,tar):
            if tar==0:
                res.append(path[:])
                return 
            for j in range(i,len(candidates)):
                if candidates[j] > tar:
                    continue
                comb(path+[candidates[j]],j,tar-candidates[j])
             
        
        comb([],0,target)
        return res
        