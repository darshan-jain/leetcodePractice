class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0 
        stack = []
        left= [0] * len(heights)
        right = [0]* len(heights)

        for i in range(len(heights)):
            if not stack:
                left[i] = 0 
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                left[i] = 0 if not stack else stack[-1]+1
                stack.append(i)
        
        print(left)
        stack = []

        for i in range(len(heights)-1,-1,-1):
            if not stack:
                right[i] = len(heights)-1
                stack.append(i)
            else:
                while stack and heights[stack[-1]] >= heights[i]:
                    stack.pop()
                right[i] = len(heights)-1 if not stack else stack[-1]-1
                stack.append(i)
        print(left)
        print(right)
        
        for i in range(len(left)):
            area = heights[i] * (right[i] - left[i] + 1)
            maxarea = max(maxarea,area)
        return maxarea



        