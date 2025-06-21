class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int low = 0 ;
        int high = matrix.size()-1;
        int j = matrix[0].size()-1;
        int row = -1;
        while(low<high){
            int mid = (low+high)/2;
            if(matrix[mid][j]==target){
                return true;
            }
            else if(matrix[mid][j]>target){
                high = mid;
            }
            else{
                low = mid+1;
            }

        }
        row = low;
        cout<<row<<" ";

        //2nd binary search
        int l = 0 ;
        int r = matrix[0].size()-1;
        while(l<=r){
            int m = (l+r)/2;
            if(matrix[row][m]==target){
                return true;
            }
            else if(matrix[row][m]>target){
                r = m-1;
            }
            else{
                l = m+1;
            }
        }
        return false;
        
    }
};