import math
from typing import List

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        samept = 0
        angles = []

        lx, ly = location

        for x, y in points:
            if x == lx and y == ly:
                samept += 1
            else:
                dx = x - lx
                dy = y - ly
                ang = math.degrees(math.atan2(dy, dx))
                angles.append(ang)

        angles.sort()
        temp = angles + [a + 360 for a in angles]

        l = 0
        res = 0
        for r in range(len(temp)):
            while temp[r] - temp[l] > angle:
                l += 1
            res = max(res, r - l + 1)

        return res + samept