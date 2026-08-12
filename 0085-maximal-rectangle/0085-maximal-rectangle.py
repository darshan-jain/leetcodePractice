class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        right = []
        left = []
        stack = []
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[stack[-1]]>=heights[i]:
                stack.pop()
            if not stack:
                right.append(len(heights))
            else:
                right.append(stack[-1])
            stack.append(i)
        right=right[::-1]

        stack = []

        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                stack.pop()
            if not stack:
                left.append(-1)
            else:
                left.append(stack[-1])
            stack.append(i)
        print(right,left)
        area = []
        for i in range(len(left)):
            val = heights[i]*(right[i] - left[i]-1)
            area.append(val)
        return max(area)
        
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        h = [0]* cols 
        ans = 0 
        for row in range(rows):
            for i,num in enumerate(matrix[row]):
                h[i] = 0 if num=="0" else h[i]+1
            ans = max(ans, self.largestRectangleArea(h))
        return ans

        