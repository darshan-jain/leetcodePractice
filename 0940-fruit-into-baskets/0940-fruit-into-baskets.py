class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm = {}
        left=0 
        right = 0 
        maxfruits = 0 

        for right in range(0,len(fruits)):
            hm[fruits[right]] = 1+ hm.get(fruits[right], 0)

            while len(hm)>2:
                fruitcount = hm[fruits[left]]
                if fruitcount==1:
                    del hm[fruits[left]]
                else:
                    hm[fruits[left]]-=1
                left+=1
            
            maxfruits = max(maxfruits, right-left+1)
        return maxfruits
        