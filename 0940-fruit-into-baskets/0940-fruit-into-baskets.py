class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = {}
        l = 0 
        r = 0 
        maxfruitcnt = 0 
        while r<len(fruits):
            hm[fruits[r]]=1+hm.get(fruits[r],0)
            if len(hm)>2:
                hm[fruits[l]]-=1
                if hm[fruits[l]]==0:
                    del hm[fruits[l]]
                l+=1
            maxfruitcnt = max(maxfruitcnt, r-l+1)
            r+=1
        return maxfruitcnt
        