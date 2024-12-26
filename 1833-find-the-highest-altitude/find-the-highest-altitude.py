class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        i=0
        for g in gain:
            res.append(res[i]+g)
            i+=1
        
        return max(res)


        