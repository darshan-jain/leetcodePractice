class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        unordered_map<int, unordered_set<int>> row,col;
        map<pair<int, int>, unordered_set<int>> sq;
        for(int i= 0;i<9;i++)
        {
            for (int j = 0;j<9;j++){
                if (board[i][j]=='.')
                continue;
                int val = int(board[i][j]);
                if ( (row[i].find(val)!=row[i].end()) || (col[j].find(val)!=col[i].end()) || (sq[{floor(i/3), floor(j/3)}].find(val)!=sq[{floor(i/3), floor(j/3)}].end()) ){
                    return false;
                }
                row[i].insert(val);
                col[j].insert(val);
                sq[{floor(i/3), floor(j/3)}].insert(val);
            }
        }
        return true;
        
    }
};