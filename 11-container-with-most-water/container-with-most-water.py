class Solution:
    def maxArea(self, height: List[int]) -> int:
        beg = 0 
        end = len(height)-1
        maxarea = 0 
        while beg < end:
            maxarea = max(maxarea, min(height[beg],height[end])*(end-beg))        
            if height[beg]>height[end]:
                end = end-1
            else:
                beg = beg+1
        
        return maxarea