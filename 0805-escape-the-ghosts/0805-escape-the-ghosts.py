class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        mindist = float("inf")
        def dist(x1,y1,x2,y2):
            return abs(x1-x2) + abs(y1-y2)
        
        for coord in ghosts:
            x1 = coord[0]
            y1 = coord[1]
            mindist = min(mindist, dist(x1,y1, target[0], target[1]))
        print(mindist)
        if mindist <= dist(0,0,target[0], target[1]):
            return False
        return True
        