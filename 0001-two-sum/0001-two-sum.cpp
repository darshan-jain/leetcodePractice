using namespace std;
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> hm;
        vector<int> res;
        for(int i=0;i<nums.size();i++){
            int a = nums[i];
            int diff = target - a;
            if (hm.find(diff)!=hm.end()){
                int bindex = hm[diff];
                res.push_back(i);
                res.push_back(bindex);
                return res;
            }
            hm[a] = i;
        }
        return res;
        
    }
};