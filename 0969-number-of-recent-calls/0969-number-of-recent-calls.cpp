class RecentCounter {
public:
    deque<int> vals;
    RecentCounter() {
        
    }
    
    int ping(int t) {
        vals.push_back(t);
        while(vals.front()<(t-3000))
        {
            vals.pop_front();
        }
        return vals.size();
        
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */