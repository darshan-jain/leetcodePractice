class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> res, left,right;
        int n = nums.size();
        left.push_back(1);
        for(int i = 0 ;i<n-1;i++){
            int val = nums[i]*left.back();
            left.push_back(val);
        }
        right.push_back(1);
        for (int i= n-1;i>0;i--){
            int val = nums[i]*right.back();
            right.push_back(val);
        }
        
        for(int i=0;i<n;i++){
            res.push_back(left[i]*right[n-i-1]);
        }
        return res;

        
    }
};