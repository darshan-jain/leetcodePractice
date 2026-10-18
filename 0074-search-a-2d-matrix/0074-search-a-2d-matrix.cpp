/*
     0,1,2,3
0   [[1,3,5,7],
1   [10,11,16,20],
2.  [23,30,34,60]]

*/

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {

        int l = 0;
        int rows = matrix.size();
        int cols = matrix[0].size();
        int r = rows*cols-1;
        while(l<=r){
            int m = (l+r)/2;
            int val = matrix[(int)m/cols][m%cols];
            if (val==target){
                return true;
            }
            else if(val>target){
                r=m-1;
            }
            else{
                l = m+1;
            }

        }

        return false;

        
    }
};