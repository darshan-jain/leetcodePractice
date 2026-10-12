class Solution {
public:
    int hammingWeight(int n) {
        int cnt = 0 ;
        int num=1;
        while(n>0)
        {
            int val = n & num;
            cnt+=val;
            n = n>>1;
        }
        return cnt; 
    }
};