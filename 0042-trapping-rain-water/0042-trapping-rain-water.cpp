class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0 ;
        int right = height.size()-1;
        int leftMax = height[left];
        int rightMax = height[right];
        int water = 0 ;
        while(left<right)
        {
            if(leftMax<rightMax)
            {
                water+=leftMax - height[left];
                left++;
                leftMax = max(leftMax, height[left]);
            }
            else{
                water+=rightMax - height[right];
                right--;
                rightMax = max(rightMax, height[right]);
            }
        }

        return water;

        
    }
};