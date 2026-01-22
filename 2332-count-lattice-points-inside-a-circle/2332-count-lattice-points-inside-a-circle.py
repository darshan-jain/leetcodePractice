class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res = set()
        for item in circles:
            x,y,r = item[0], item[1], item[2]
        
            minx,maxx = x-r, x+r
            miny,maxy = y-r, y+r

            for i in range(minx,maxx+1):
                for j in range(miny,maxy+1):
                    if (i-x)**2 + (j-y)**2 <= r**2 :
                        if (i,j) not in res:
                            res.add((i,j))
        print(res)
        return len(res)

