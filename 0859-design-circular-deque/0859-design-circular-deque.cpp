class MyCircularDeque {
public:
    vector<int> res;
    int head;
    int tail;
    int size;
    int cap;
    MyCircularDeque(int k) {
        for(int i=0;i<k;i++)
        {
            res.push_back(0);
        }
        head =0;
        tail = 0;
        size=0;
        cap=k;
        
    }
    
    bool insertFront(int value) {
        if(isFull())
        {
            return false;
        }
        res[head] = value;
        head = (head-1+cap)%cap;
        if(size==0)
        tail = (tail+1+cap)%cap;
        size++;
        return true;
        
    }
    
    bool insertLast(int value) {
        if(isFull())
        {
            return false;
        }
        res[tail] = value;
        tail = (tail+1+cap)%cap;
        if (size==0)
        head = (head-1+cap)%cap;
        size++;
        return true;
        
    }
    
    bool deleteFront() {
        if(isEmpty())
        {
            return false;
        }
        head = (head+1+cap)%cap;
        size--;
        if(isEmpty())
        {
            head=0;
            tail = 0;
        }
        return true;
        
    }
    
    bool deleteLast() {
        if(isEmpty())
        {
            return false;
        }
        tail = (tail-1+cap)%cap;
        size--;
        if(isEmpty())
        {
            head=0;
            tail = 0;
        }
        return true;
        
    }
    
    int getFront() {
        if (isEmpty())
        {
            return -1;
        }
        return res[(head+1+cap)%cap];
        
    }
    
    int getRear() {
        if (isEmpty())
        {
            return -1;
        }
        return res[(tail-1+cap)%cap];
        
    }
    
    bool isEmpty() {
        return size==0;
        
    }
    
    bool isFull() {
        return size==cap;
        
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */