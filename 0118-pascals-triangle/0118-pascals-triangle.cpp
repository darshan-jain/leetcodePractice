class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<int> row;
        vector<vector<int>> ans;
        if(numRows==0){
            return ans;
        }

        row.push_back(1);
        ans.push_back(row);
        for(int i=2;i<=numRows;i++){
            vector<int> temp;
            temp.push_back(0);
            for(auto it:row){
                temp.push_back(it);
            }
            temp.push_back(0);
            row.clear();
            for(int j=0;j<=temp.size()-2;j++){
                row.push_back(temp[j]+temp[j+1]);
            }
            ans.push_back(row);
        }
        return ans;
    }
};