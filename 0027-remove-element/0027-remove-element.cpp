class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int i=0;
        int leng = 0 ;
        for(i=0;i<nums.size();i++){
            if(nums[i]!=val)
            {nums[leng]=nums[i];
            leng++;
            }
        }
        return leng;
        
    }
};