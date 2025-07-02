class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0 ;
        int j = -1;
        unordered_map<char, int> mpp;
        for(int i=0;i<s.size();i++)
        {
            char c = s[i];
            if(mpp.find(c)!=mpp.end())
            j = max(j,mpp[c]);
            else
            j = max(j,-1);
            ans = max(ans,i-j);
            mpp[c]=i;
        }
        return ans;

        
    }
};