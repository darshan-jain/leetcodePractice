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
        
        int ans=0;
        double prev = 0 ;
        for(int i = 0; i < arr.size(); i++){
            int pos = arr[i][0];
            int sp = arr[i][1];
            // FIX 2: Perform double precision division
            double t = (double)(target - pos) / sp; 
            if(t>prev){
                ans++;
                prev = t;
            }
            
        }
        return ans;
        
        // FIX 3: Change stack type to double to match your time array
       
       
    }
};
