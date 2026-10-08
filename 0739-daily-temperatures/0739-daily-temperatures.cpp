class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        vector<int> res; 
        stack<int> stack;
        int n = temperatures.size();
        for(int i=n-1;i>=0;i--)
        {
            while(!stack.empty() and temperatures[stack.top()]<=temperatures[i] ){
                stack.pop();
            }
            if(!stack.empty()){
                res.push_back(stack.top()-i);
            }
            else{
                res.push_back(0);
            }
            stack.push(i);
        }
        reverse(res.begin(), res.end());
        return res;
        
    }
};