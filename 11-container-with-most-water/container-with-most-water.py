class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        beg = 0
        end = len(height)-1
        max_area =0 
        while beg<end:
            max_area = max(max_area,min(height[beg],height[end])*(end-beg))
            if height[beg]>height[end]:
                end = end-1
            else:
                beg = beg+1
        return max_area