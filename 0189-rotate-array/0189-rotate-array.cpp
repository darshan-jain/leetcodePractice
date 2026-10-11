class Solution {
public:
    void rr(vector<int>& nums, int start, int end)
        {
            while(start<=end)
            {
                int temp = nums[start];
                nums[start]= nums[end];
                nums[end]=temp;
                start++;
                end--;
            }
        }
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k%n;

        rr(nums, 0, nums.size()-1);
        rr(nums, 0,k-1);
        rr(nums, k, nums.size()-1);
        
        
    }
};