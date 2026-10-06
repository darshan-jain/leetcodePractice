class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> s;
        unordered_map<char, int> t;
        int s1size = s1.size();
        int s2size = s2.size();
        if (s2size < s1size){
            string temp = s1;
            s1 = s2;
            s2 = temp;
        }
        for(int i=0;i<s1size;i++)
        {
            s[s1[i]]++;
            t[s2[i]]++;
        }

        int r = s1size;
        int l = 0;
        while(r<s2size){
            if(s==t)
            return true;
            t[s2[r]]++;
            t[s2[l]]--;
            if (t[s2[l]]==0){
            t.erase(s2[l]);
            }
            r+=1;
            l+=1;
        }
        if(s==t)
        return true;
        
        return false;

        
    }
};