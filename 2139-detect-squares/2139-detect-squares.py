class DetectSquares:

    def __init__(self):
        self.ds = defaultdict(int)
        self.pts = []
        

    def add(self, point: List[int]) -> None:
        self.ds[tuple(point)]+=1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        res = 0 
        px,py = point
        for x,y in self.pts:
            if (abs(px-x)==abs(py-y)) and x!=px and y!=py:
                if (x,py) in self.ds and (px,y) in self.ds:
                    res+=self.ds[(x,py)]*self.ds[(px,y)]
        return res
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)