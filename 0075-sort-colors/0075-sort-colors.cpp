class Solution {
public:
    void sortColors(vector<int>& nums) {
        // map<int,int> mpp;
        // for(int i=0;i<nums.size();i++){
        //     mpp[nums[i]]++;
        // }
        // nums.clear();
        // for(auto it:mpp){
        //     //cout<<it.first<<" "<<it.second<<endl;
        //     int i=1;
        //     for(i=1;i<=it.second;i++){
        //         nums.push_back(it.first);
        //     }
        // }

        //One pass approach - Dutch Flag Problem
        int low=0;
        int mid=0;
        int high = nums.size()-1;
        while(mid<=high){
            if(nums[mid]==0){
                swap(nums[low],nums[mid]);
                low++;
                mid++;
            }
            else if(nums[mid]==1)
            mid++;
            else
            {
                swap(nums[mid],nums[high]);
                high--;
            }
        }

        }

    
};