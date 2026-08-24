class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        hm1o = {}
        hm1e = {}
        hm2e = {}
        hm2o = {}
        for i,c in enumerate(s1):
            if i%2==0:
                hm1e[c]=1+hm1e.get(c,0)
            else:
                hm1o[c]=1+hm1o.get(c,0)
        
        for i,c in enumerate(s2):
            if i%2==0:
                hm2e[c]=1+hm2e.get(c,0)
            else:
                hm2o[c]=1+hm2o.get(c,0)
        shm1e = sorted(hm1e.items())
        shm1o = sorted(hm1o.items())
        shm2o = sorted(hm2o.items())
        shm2e = sorted(hm2e.items())
        return shm1e == shm2e and shm1o == shm2o
            

        