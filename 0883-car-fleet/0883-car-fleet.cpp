class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<vector<int>> arr;
        for(int i = 0; i < position.size(); i++) {
            arr.push_back({position[i], speed[i]});
        }
        sort(arr.begin(), arr.end());
        reverse(arr.begin(), arr.end());
        
        // FIX 1: Change vector type to double to prevent truncation
        vector<double> res; 
        for(int i = 0; i < arr.size(); i++){
            int pos = arr[i][0];
            int sp = arr[i][1];
            // FIX 2: Perform double precision division
            double t = (double)(target - pos) / sp; 
            res.push_back(t);
        }
        
        // FIX 3: Change stack type to double to match your time array
        stack<double> st; 
        for(int i = 0; i < res.size(); i++) {
            if(st.empty()){
                st.push(res[i]);
            }
            else if(res[i] > st.top()){
                st.push(res[i]);
            }
            else{
                continue;
            }
        }
        return st.size();
    }
};
