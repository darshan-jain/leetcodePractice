class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m==n && m==1)
        {
            return 1;
        }
        vector<int> vec;
        vector<vector<int>> dp;
        for(int i=0;i<m;i++)
         {   for(int j=0;j<n;j++)
            vec.push_back(1);
            dp.push_back(vec);
         }
        
        for(int i=1;i<m;i++)
        {
            for(int j=1;j<n;j++)
            {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }

        return dp[m-1][n-1];
        
    }
};