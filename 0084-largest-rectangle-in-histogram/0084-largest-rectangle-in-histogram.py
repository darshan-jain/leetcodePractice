class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        maxarea = 0
        stack = []
        n = len(height)
        left = [0]*n
        right = [0]*n

        for i in range(n):
            if not stack:
                left[i] = 0 
                stack.append(i)
            else:
                while stack and height[stack[-1]]>=height[i]:
                    stack.pop()
                left[i] = 0 if not stack else stack[-1]+1
                stack.append(i)
        
        stack = []
        for i in range(n-1,-1,-1):
            if not stack:
                right[i] = n-1
                stack.append(i)
            else:
                while stack and height[stack[-1]]>=height[i]:
                    stack.pop()
                right[i] = n-1 if not stack else stack[-1]-1
                stack.append(i)
        
        for i in range(n):
            maxarea = max(maxarea, height[i]*(right[i] - left[i] + 1) )
        return maxarea

        