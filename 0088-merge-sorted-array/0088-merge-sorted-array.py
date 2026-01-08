class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #             j     insertpos                i 
        # nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3

        # Output: [1,2,2,3,5,6]

        # Compare j and i and insert

        j = m-1
        i = n-1
        insertpos = m+n-1
        while j>=0 and i>=0:
            #item from nums1 is used
            if nums1[j] >= nums2[i]:
                nums1[insertpos] = nums1[j]
                insertpos-=1
                j-=1
            else:
                nums1[insertpos] = nums2[i]
                insertpos-=1
                i-=1
        while j>=0:
            nums1[insertpos] = nums1[j]
            insertpos-=1
            j-=1

        while i>=0:
            nums1[insertpos] = nums2[i]
            insertpos-=1
            i-=1
        

        