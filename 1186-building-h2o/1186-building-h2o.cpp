#include <mutex>
#include <condition_variable>
#include <functional>
class H2O {
    private:
    mutex mtx;
    condition_variable cv;
    int hCount = 0 ;
    int oCount = 0 ;
public:
    H2O() {
    }

    void hydrogen(function<void()> releaseHydrogen) {
        unique_lock<mutex> lock(mtx);

        while(!(hCount<2)){
            cv.wait(lock);
        }
        
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();
        hCount+=1;
        if (hCount==2 && oCount==1){
            hCount=0;
            oCount=0;
        }
        cv.notify_all();
    }

    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lock(mtx);

        while(!(oCount<1)){
            cv.wait(lock);
        }

        
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();
        oCount+=1;

        if (hCount==2 && oCount==1){
            hCount=0;
            oCount=0;
        }
        cv.notify_all();
    }
};