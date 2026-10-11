class MyHashMap {
public:
    int MOD;
    vector<int> arr;
    MyHashMap() {
        MOD = 100000;
        for(int i=0;i<MOD;i++)
        {
            arr.push_back(-1);
        }
        
    }
    
    void put(int key, int value) {
        int h = key%MOD;
        arr[h] = value;
        
    }
    
    int get(int key) {
        int h=key%MOD;
        return arr[h];
        
    }
    
    void remove(int key) {
        int h = key%MOD;
        arr[h]=-1;
        
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */