class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> hm;
        string sword = "";
        for(auto& word:strs){
            sword = word;
            sort(sword.begin(), sword.end());
            hm[sword].push_back(word);
        }
        
        for (auto& [key,value]:hm){
            res.push_back(value);
        }
        return res;
        
    }
};