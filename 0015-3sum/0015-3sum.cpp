class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        sort(nums.begin(), nums.end());
        int n = nums.size();
        for(int i = 0 ;i<n-2;i++){
            if (i>0 && nums[i]==nums[i-1])
            continue;
            int j=i+1;
            int k = n-1;
            while(j<k){
                int tot = nums[i] + nums[j] + nums[k];
                if (tot>0)
                k-=1;
                else if (tot<0)
                j+=1;
                else{
                    res.push_back({nums[i], nums[j], nums[k]});
                    j+=1;
                    while(j<k && nums[j]==nums[j-1]){
                        j+=1;
                    }
                }
            }
        }
        return res;
        
    }
};