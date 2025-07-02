class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int,int> mpp;
        int res = 0 ;
        int diff = 0 ;
        int curSum = 0 ;
        mpp[0]=1;

        for(auto n: nums)
        {
            curSum+=n;
            
            diff = curSum - k;
            if(mpp.find(diff)!=mpp.end()){
                res+=mpp[diff];
            }
            mpp[curSum]++;
        }
        return res;
        
    }
};