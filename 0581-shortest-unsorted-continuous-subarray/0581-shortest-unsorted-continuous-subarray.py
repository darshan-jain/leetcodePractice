class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        maxarr=[]
        for i in range(len(nums)):
            if not maxarr:
                maxarr.append(nums[i])
            else:
                maxarr.append(max(maxarr[-1],nums[i]))
        print(maxarr)

        minarr = []
        for i in range(len(nums)-1,-1,-1):
            if not minarr:
                minarr.append(nums[i])
            else:
                minarr.append(min(minarr[-1], nums[i]))
        minarr = minarr[::-1]
        idx1=-1
        for i in range(len(nums)):
            if minarr[i]!=maxarr[i]:
                idx1=i
                break
        idx2=len(nums)
        for i in range(len(nums)-1,-1,-1):
            if maxarr[i]!=minarr[i]:
                idx2=i
                break
        res = idx2-idx1+1
        if res > len(nums):
            return 0 
        return res
        