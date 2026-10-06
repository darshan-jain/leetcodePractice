class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int ans = 0;
        unordered_map<char, int> hm;
        int j=-1;
        int i = 0 ;
        while(i<s.size()){
            j = max(j, hm.count(s[i])? hm[s[i]]:-1);
            ans = max(ans, i-j);
            hm[s[i]]=i;
            i+=1;
        }
        return ans;
        
    }
};