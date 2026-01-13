class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0 
        n = len(heights)
        left = [0]*n
        right = [0]*n
        stack = []

        for i in range(n):
            if not stack:
                left[i] = 0 
                stack.append(i)
            else:
                while stack and heights[stack[-1]]>=heights[i]:
                    stack.pop()
                left[i] = 0 if not stack else stack[-1]+1
                stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            if not stack:
                right[i] = n-1
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                right[i] = n-1 if not stack else stack[-1]-1
                stack.append(i)
        
        for i in range(n):
            maxarea = max(maxarea, heights[i]*(right[i]-left[i]+1))
        return maxarea
        