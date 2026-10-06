class Solution {
public:
    bool isPalindrome(string s) {
        string news = "";
        for(auto& c :s){
            if (isdigit(c) || isalpha(c)){
                news+=tolower(c);
            }
        }
        int l = 0;
        int r = news.size()-1;
        while(l<=r){
            if(news[l]!=news[r]){
                return false;
            }
            l+=1;
            r-=1;
        }
        return true;
        
    }
};