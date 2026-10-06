class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> ans;
        priority_queue<pair<int,int>> heap;
        for(int i= 0;i<k;i++){
            heap.push({nums[i],i});
        }
        pair <int, int> top = heap.top();
        ans.push_back(top.first);
        for(int i= k;i<nums.size();i++)
        {
            
            while(heap.size()>=1 and heap.top().second<=i-k)
            {
                heap.pop();
            }
            heap.push({nums[i],i});
            pair <int, int> top = heap.top();
            ans.push_back(top.first);


        }
        return ans;
        
    }
};