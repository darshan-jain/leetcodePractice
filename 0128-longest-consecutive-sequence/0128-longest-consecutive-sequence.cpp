class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> val;
        for (auto num:nums){
            val.insert(num);
        }
        int curLen = 0;
        int maxLen = 0;
        for(auto num:val){
            curLen=1;
            int curNum = num;
            if (!val.contains(curNum-1)){
                while (val.contains(curNum+1)){
                    curLen++;
                    curNum++;
                }
                maxLen = max(maxLen, curLen);
            }
        }
        return maxLen;
        
    }
};