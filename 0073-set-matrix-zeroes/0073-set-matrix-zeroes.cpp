class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int rowFlag = 0 ;
        int colFlag =0 ;
        for(int row = 0 ; row<matrix.size();row++){
            for(int col=0;col<matrix[0].size();col++){
                if(matrix[row][col]==0){
                    if(row==0)
                    rowFlag = 1;
                    if(col==0)
                    colFlag=1;
                    else{
                        if(row!=0 && col!=0)
                        {
                            matrix[0][col]=0;
                            matrix[row][0]=0;
                        }
                    }
                }
            }
        }

        for(int i=1;i<matrix.size();i++){
            for(int j=1;j<matrix[0].size();j++){
                if(matrix[i][0]==0 || matrix[0][j]==0){
                    matrix[i][j]=0;
                }
            }
        }

        if(rowFlag){
            for(int j=0;j<matrix[0].size();j++)
            {
                matrix[0][j]=0;
            }
        }

        if(colFlag){
            for(int i=0;i<matrix.size();i++){
                matrix[i][0]=0;
            }
        }
        
    }
};