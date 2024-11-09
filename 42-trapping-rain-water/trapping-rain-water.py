class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Multi Pass Approach
        # n = len(height)
        # left_max = [0]*n
        # right_max = [0]*n
        # water_trapped = 0
        # left_max[0] = height[0]
        # for i in range(1,n):
        #     left_max[i] = max(left_max[i-1],height[i])
        
        # right_max[-1] = height[-1]
        # for i in range(n-2,-1,-1):
        #     right_max[i] = max(right_max[i+1],height[i])
        
        # for i in range(n):
        #     water_trapped += min(left_max[i],right_max[i])-height[i]
        
        # return water_trapped

        #One Pass Approach
        left,right = 0, len(height)-1
        leftmax, rightmax = height[left],height[right]
        watertrapped = 0
        while left< right:
            if leftmax<rightmax:
                watertrapped+=leftmax-height[left]
                left+=1
                leftmax= max(leftmax,height[left])
            else:
                watertrapped+=rightmax - height[right]
                right-=1
                rightmax=max(rightmax,height[right])
        return watertrapped