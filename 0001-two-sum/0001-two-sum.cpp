class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hm;
        for(int i=0;i<nums.size();i++)
        {
            int diff = target - nums[i];
            //diff is present
            if(hm.find(diff)!=hm.end()){
                return {i,hm[diff]};
            }
            hm[nums[i]]=i;
        }
        return {-1,-1};
        
    }
};