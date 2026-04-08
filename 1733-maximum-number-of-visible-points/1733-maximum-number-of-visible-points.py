import math
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        samept = 0 
        angles = []
        for x,y in points:
            diffx = x - location[0]
            diffy = y - location[1]
            if diffx==0 and diffy==0:
                samept+=1
                continue
            angles.append(math.degrees(math.atan2(diffy,diffx)))
        
        angles.sort()
        temp = angles + [a+360 for a in angles]

        l= 0 
        r = 0 
        res = 0 
        while r < len(temp):
            while temp[r]- temp[l] > angle:
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res + samept


        