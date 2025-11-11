class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)-1
        leftMax = height[0]
        rightMax = height[n]
        left = 0 
        right = n
        water = 0 
        while left<right:
            if leftMax<rightMax:
                water+=(leftMax-height[left])
                left+=1
                leftMax = max(leftMax, height[left])
            else:
                water+=(rightMax - height[right])
                right-=1
                rightMax = max(rightMax,height[right])
        return water
        