class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        stack<int> st; 
        vector<int> res; 
        for(int i=0;i<n;i++)
        res.push_back(0);
        int prev = 0;
        for(auto& log: logs)
        {
            auto result = log | std::views::split(':') | std::ranges::to<std::vector<std::string>>();
            int fid = stoi( result[0]);
            string s = result[1];
            int time = stoi(result[2]);

            if(s=="start")
            {
                if(st.size()>0)
                {
                    res[st.top()]+=time-prev;
                }
                st.push(fid);
                prev = time;
            }
            else{
                res[st.top()]+=time - prev+1;
                st.pop();
                prev = time+1;
            }

        }
        return res; 
        
    }
};