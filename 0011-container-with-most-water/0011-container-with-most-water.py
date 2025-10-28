class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = - 1
        l = 0 
        r = len(height)-1
        while l < r:
            h = min(height[l], height[r])
            b = r-l

            area = b*h
            res = max(area,res)
            if h == height[l]:
                l+=1
            else:
                r-=1
        return res
        