using namespace std;
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int> bag;
        for (auto& num : nums){
            if (bag.find(num)!= bag.end()){
                return true;
            }
            bag.insert(num);
        }
        return false;

        
    }
};