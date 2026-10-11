class Node{
    public:
    int key;
    int value;
    Node* prev;
    Node* next;
    
    Node(int k, int v){
        value = v;
        key = k;
    }

};
class LRUCache {
public:
int cap;
unordered_map<int, Node*> cache;
Node* leftNode;
Node* rightNode;


    LRUCache(int capacity) {
        cap = capacity;
        leftNode = new Node(0,0);
        rightNode = new Node(0,0);
        leftNode->next = rightNode;
        rightNode->prev = leftNode;
        
        
    }

    void insert(Node* node){
        Node* last = rightNode;
        Node* prev = rightNode->prev;
        prev->next = node;
        node->prev = prev;
        last->prev = node;
        node->next = last;

    }

    void remove(Node* node)
    {
        Node* first = node->prev;
        Node* sec = node->next;
        first->next = sec;
        sec->prev = first;

    }
    
    int get(int key) {
        //Doesn't exist
        if (cache.find(key)==cache.end())
        {
            return -1;
        }
        //exists
        Node* node = cache[key];
        remove(node);
        insert(node);
        int val = node->value;
        return val;
        
    }
    
    void put(int key, int value) {
        if(cache.find(key)!=cache.end())
        {
            Node* oldnode = cache[key];
            remove(oldnode);

        }
        Node* newnode= new Node(key,value);
        insert(newnode);
        cache[key] = newnode;
        
        if(cache.size()>cap)
        {
            Node* lru = leftNode->next;
            remove(lru);
            cache.erase(lru->key); // should be key here 
        }

        
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */