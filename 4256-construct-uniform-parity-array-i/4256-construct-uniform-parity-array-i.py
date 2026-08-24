class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        n = len(nums1)
        nums2 = [0]*n
        # oddc = 0 
        # evenc = 0 
        # for num in nums1:
        #     if num%2==0:
        #         evenc+=1
        #     else:
        #         oddc+=1
        # isOdd = False 
        # if oddc >= evenc:
        #     isOdd = True
        #if isOdd - fill with odd nos 
        
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
        return helpOdd() or helpeven()
        
        