class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ans;
        sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
        
        if (a.empty() || b.empty()) {
            return false; // Or a more robust comparison for empty vectors
        }
        return a[0] < b[0]; // Sorts in ascending order based on the first element
    });
    ans.push_back(intervals[0]);
    vector<int> lastval ;
    for(int i=0;i<intervals.size();i++){
        lastval= ans.back();
        if(lastval[1] >= intervals[i][0]){
            //merge
            if(lastval[1] < intervals[i][1]){
                lastval[1] = intervals[i][1];
                ans.back() = lastval;
            }
        }
        else{
            ans.push_back(intervals[i]);
        }

    }
    
    return ans;


    }
};