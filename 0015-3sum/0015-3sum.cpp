class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(),nums.end());

        vector<int> sol;
        vector<vector<int>> ans;
        int i=0;
        for(i=0;i<nums.size()-2;i++)
        {
            if (i>0 && nums[i]==nums[i-1])
            continue;
            int j=i+1;
            int k = nums.size()-1;
            while(j<k)
            {
                int total = nums[i]+nums[j]+nums[k];

                if(total>0)
                {
                    k--;
                }
                else if (total<0)
                {
                    j++;
                }
                else{
                    sol.push_back(nums[i]);
                    sol.push_back(nums[j]);
                    sol.push_back(nums[k]);
                    ans.push_back(sol);
                    sol.clear();

                    j++;
                    k--;
                    while(j<k && nums[j]==nums[j-1])
                    j++;

                }
                
                

            }
        }
        return ans;
    }
};