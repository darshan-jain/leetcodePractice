class Solution {
public:
    int reverse(int x) {
        
        long long res= 0 ;
        while(x!=0)
        {
            int digit = x%10;
            res= res*10 + digit;
            x = x/10;
            
        }
        
        if(res < pow(-2,31) || res > pow(2,31)-1)
        return 0;
        return res; 
        
    }
};