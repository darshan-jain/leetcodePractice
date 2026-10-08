class Solution {
public:
    bool isValid(string s) {
        stack<int> st;
        for(auto& c:s){
            if (c=='(')
            st.push(')');
            else if (c=='{')
            st.push('}');
            else if (c == '[')
            st.push(']');
            else{
                if (st.empty())
                return false;
                else if (st.top()!=c)
                return false;
                else
                st.pop();
            }
        }
        if (st.empty())
        return true;
        else
        return false;
        
    }
};