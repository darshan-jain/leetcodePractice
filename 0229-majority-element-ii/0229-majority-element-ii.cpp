class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int cnt1=0;
        int cnt2=0;
        int elem1 = INT_MIN;
        int elem2= INT_MIN;
        int n = nums.size();
        for(int i=0;i<nums.size();i++){
            if(cnt1==0 && elem2!=nums[i]){
                cnt1=1;
                elem1=nums[i];
            }
            else if(cnt2==0 && elem1!=nums[i]){
                cnt2=1;
                elem2 = nums[i];
            }
            else if(elem1==nums[i])cnt1++;
            else if(elem2==nums[i])cnt2++;
            else
            {
                cnt1--;
                cnt2--;
            }
        }

        vector<int> ans;
        cnt1=0;
        cnt2=0;
        for(int i=0;i<nums.size();i++)
        {
            if(elem1==nums[i])cnt1++;
            if(elem2==nums[i])cnt2++;
        }

        int val = n/3;
        if(cnt1>val)
            ans.push_back(elem1);
        if(cnt2>val)
        ans.push_back(elem2);

return ans;
        
    }
};