class Solution {
public:
    int maxArea(vector<int>& height) {
        int maxwater = 0 ;
        int l = 0;
        int r = height.size()-1;

        while(l<r){
            if (height[l]>=height[r]){
                int h = height[r];
                int b = (r-l);
                maxwater = max(maxwater, h*b);
                r-=1;
            }
            else{
                int h = height[l];
                int b = (r-l);
                maxwater = max(maxwater, h*b);
                l+=1;
            }
            
        }
        return maxwater;
        
    }
};