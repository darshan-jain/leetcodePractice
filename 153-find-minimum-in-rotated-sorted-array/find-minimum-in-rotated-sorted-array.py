class Solution(object):

    def helper(self,beg,end,nums):
        if end <= beg:
            return nums[end]
        mid = (beg+end)//2
        if nums[mid] > nums[end]:
            return self.helper(mid+1,end,nums)
        else:
            return self.helper(beg,mid,nums)
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #Recursive Approach 
        return self.helper(0,len(nums)-1,nums)

        #Iterative Approach

        # beg,end = 0, len(nums)-1
        
        # while beg<end:
        #     mid = (beg+end)//2
        #     if nums[mid] > nums[end]:
        #         beg = mid+1
        #     else:
        #         end = mid
            
        # return nums[beg]
            
            