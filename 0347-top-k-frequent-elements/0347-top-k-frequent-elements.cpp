class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hm;
        for (int i=0;i<nums.size(); i++){
            hm[nums[i]]++;
        }
        priority_queue<pair<int, int>> maxheap;
        for(auto& [key,value]: hm){
            maxheap.push({value,key});
        }
        vector<int> res;
        while (k>0){
            pair<int, int> toppair;
            toppair = maxheap.top();
            res.push_back(toppair.second);
            k--;
            maxheap.pop();
        }
        return res;
        
    }
};