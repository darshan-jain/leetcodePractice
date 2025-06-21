class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // unordered_map<int,int> mpp;
        // for(int i=0;i<nums.size();i++){
        //     if(mpp[nums[i]]>0)
        //     {return nums[i];}
        //     else{mpp[nums[i]]++;}
        // }
        // return 0;

        //optimal approach
        //treat the problem like a graph 
        //node - index value and next node - value at index
        //if duplicate exists then cycle is formed
        int slow = nums[0];
        int fast = nums[0];
        do{
            slow = nums[slow];
            fast = nums[nums[fast]];
        }while(slow!=fast);

        slow = nums[0];
        while(slow!=fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        return slow;
        
    }
};