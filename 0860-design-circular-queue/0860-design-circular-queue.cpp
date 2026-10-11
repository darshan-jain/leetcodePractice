class MyCircularQueue {
public:
    vector<int> res;
    int insertpos;
    int removepos;
    int capacity;
    int size;
    
    MyCircularQueue(int k) {
        for(int i=0;i<k;i++)
        {
            res.push_back(0);
        }
        insertpos = 0;
        removepos = 0;
        capacity = k;
        size = 0;
       
        
    }
    
    bool enQueue(int value) {
        if(isFull())
        {
            return false;
        }
        res[insertpos%capacity]=value;
        insertpos+=1;
        size++;
        
        return true;
        
    }
    
    bool deQueue() {
        if(isEmpty())
        {
            return false;
        }
        removepos++;
        size--;
        return true;
        
    }
    
    int Front() {
        if(isEmpty())
        {
            return -1;
        }
        return res[removepos%capacity];

        
    }
    
    int Rear() {
        if(isEmpty())
        {
            return -1;
        }
        return res[(insertpos-1+capacity)%capacity];
        
    }
    
    bool isEmpty() {
        return size==0;
        
    }
    
    bool isFull() {
        return size==capacity;
        
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */