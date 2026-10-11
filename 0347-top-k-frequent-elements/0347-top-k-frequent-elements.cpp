class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> hm;
        for (int i=0;i<nums.size(); i++){
            hm[nums[i]]++;
        }
        priority_queue<vector<int>> maxheap;
        for(auto& [key,value]: hm){
            maxheap.push({value,key});
        }
        vector<int> res;
        while (k>0){
            vector<int> toppair;
            toppair = maxheap.top();
            res.push_back(toppair[1]);
            k--;
            maxheap.pop();
        }
        return res;
        
    }
};