class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums2 = [0]*n
       
        def helpOdd():
            for i in range(n):
                if nums1[i]%2!=0:
                    nums2[i] = nums1[i]
                else:
                    fillPos = False
                    for j in range(n):
                        if j!=i and (nums1[i]-nums1[j])%2!=0:
                            nums2[i] = nums1[i]-nums1[j]
                            fillPos = True
                            break
                    if fillPos==False:
                        return False
            return True
        def helpeven():
            for i in range(n):
                if nums1[i]%2==0:
                    nums2[i] = nums1[i]
                else:
                    fillPos = False
                    for j in range(n):
                        if j!=i and (nums1[i]-nums1[j])%2==0:
                            nums2[i] = nums1[i]-nums1[j]
                            fillPos = True
                            break
                    if fillPos == False:
                        return False
            return True
        return helpeven() or helpOdd()
        
        