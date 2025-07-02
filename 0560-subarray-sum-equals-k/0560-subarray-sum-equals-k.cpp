class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> mpp;
        int res=0;
        int diff=0;
        int curSum = 0 ;

        mpp[0]=1;
        for(int i=0;i<nums.size();i++)
        {
            curSum+=nums[i];
            diff = curSum-k;

            if(mpp.find(diff)!=mpp.end())
            {res+= mpp[diff];
            cout<<"Found"<<diff<<endl;
            }

            mpp[curSum]++;
        }
        for(auto it:mpp)
        cout<< it.first<<" "<<it.second<<endl;

        return res;
        
    }
};