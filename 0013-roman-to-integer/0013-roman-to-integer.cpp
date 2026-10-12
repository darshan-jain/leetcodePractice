class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char, int> hm;
        hm = {
            {'I', 1},
{'V'  ,          5},
{'X'   ,         10},
{'L'    ,         50},
{'C'     ,        100},
{'D'      ,       500},
{'M'       ,      1000}

        };


        int res = 0 ;
        for(int i=0;i<s.size();i++)
        {
            if (i==0)
            {
                char curr = s[i];
                res+=hm[curr];
            }
            else{
                char curr = s[i];
                char prev = s[i-1];
                if (hm[prev]<hm[curr]){
                    res-=2*hm[prev];
                }
                res+=hm[curr];

            }
        }
        return res;
        
    }
};