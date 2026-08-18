class Solution:

    def __init__(self, w: List[int]):
        self.s = [0]
        for c in w:
            self.s.append(self.s[-1]+c)
        

    def pickIndex(self) -> int:
        x = random.randint(1, self.s[-1])
        l = 0 
        r = len(self.s)-1
        while l<r:
            m = (l+r)//2
            if self.s[m] >= x:
                r = m 
            else:
                l = m+1
        return l-1
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()