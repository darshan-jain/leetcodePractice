using namespace std;
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size()!=t.size())
        return false;
        unordered_map<char, int> hms;
        unordered_map<char, int> hmt;
        for(int i=0;i<s.size();i++){
            char c = s[i];
            hms[c]++;
        }
        for (int i= 0 ;i<t.size(); i++){
            char c = t[i];
            hmt[c]++;

        }
        
        for(const auto& [key,value]:hms){
            if ((hmt.find(key)==hmt.end()) || (value!=hmt[key])){
                return false;
            }
        }
        return true;

        
    }
};