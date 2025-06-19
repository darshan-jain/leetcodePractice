class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ans;
        sort(intervals.begin(), intervals.end(), [](vector<int>&a,vector<int>&b ) {
            if(a.empty()||b.empty())
            return false;
            return a[0]<b[0];
        });

        ans.push_back(intervals[0]);
        vector<int> lastelem;
        for(int i=1;i<intervals.size();i++){
            lastelem = ans.back();
            if(lastelem[1]>= intervals[i][0]){
                //merge
                if(lastelem[1]<intervals[i][1])
                {
                    lastelem[1]=intervals[i][1];
                    ans.back() = lastelem;
                }
            }
            else{
                ans.push_back(intervals[i]);
            }

        }
        return ans;

        
    }
};