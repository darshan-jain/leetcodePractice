class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = -1
        l = 0
        r = len(height)-1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res , area)
            if height[r] <= height[l]:
                r-=1
            else:
                l+=1
        return res
        