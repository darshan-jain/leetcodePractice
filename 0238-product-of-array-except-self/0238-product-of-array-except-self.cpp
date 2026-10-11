class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector <int> res, left, right;
        left.push_back(1);
        for(int i=0;i<nums.size()-1;i++)
        {
            left.push_back(left[left.size()-1]*nums[i]);
        }
        right.push_back(1);
        for(int i= nums.size()-1;i>0;i--)
        {
            right.push_back(right[right.size()-1]*nums[i]);
        }
        reverse(right.begin(), right.end());
        for(int i=0;i<left.size();i++)
        {
            res.push_back(left[i]*right[i]);
        }
        return res; 
        
    }
};