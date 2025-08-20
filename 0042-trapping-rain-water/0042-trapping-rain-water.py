class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax = height[0]
        rightMax = height[-1]
        water = 0 
        left = 0 
        right = len(height)-1
        while left<right:
            if leftMax < rightMax:
                water+= (leftMax - height[left])
                left+=1
                leftMax = max(leftMax, height[left])
            else:
                water+= (rightMax - height[right])
                right-=1
                rightMax = max(rightMax, height[right])
        return water


        