class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        if(m==1 && n==0){
            return;
        }
        if(m==0 && n==1){
            nums1.swap(nums2);
            return;
        }
        //make sure nums1 is larger in length to nums2
        int i = m-1;
        int j = n-1;
        int ip = m+n-1;

        while (j>=0 and i>=0){
            if(nums1[i]<=nums2[j]){
                nums1[ip]=nums2[j];
                j--;
                ip--;
            }
            else{
                nums1[ip]=nums1[i];
                i--;
                ip--;
            }

        }
        while(j>=0){
            nums1[ip] = nums2[j];
            ip--;
            j--;
        }
        


        
    }
};