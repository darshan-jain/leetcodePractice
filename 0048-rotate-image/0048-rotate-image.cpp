class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {

        //swap elements along the main diagonal
        for(int i=0;i<matrix.size();i++)
        {
            for(int j=i;j<matrix[0].size();j++){
                swap(matrix[i][j],matrix[j][i]);
            }
        }

        //reverse each row
        for(int i=0;i<matrix.size();i++)
        {
            reverse(matrix[i].begin(),matrix[i].end());
        }
        
    }
};