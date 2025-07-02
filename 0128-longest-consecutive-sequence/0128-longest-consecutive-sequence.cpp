class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set;
        for(int i=0;i<nums.size();i++)
            set.insert(nums[i]);
        
        int curLen = 0 ;
        int maxLen = 0;
        int curNum;
        for(auto it : set)
        {
            curNum = it;
            if(!set.count(curNum-1)){
                curLen = 1;
                while(set.count(curNum+1)){
                    curLen++;
                    curNum++;
                    
                }
                maxLen = max(maxLen, curLen);
            }
        }
        return maxLen;

        
    }
};