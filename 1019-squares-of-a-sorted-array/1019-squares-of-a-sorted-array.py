class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0 for _ in range(len(nums))]
        l= 0 
        r = len(nums)-1
        insertpos = len(nums)-1
        while l<=r:
            val1 = nums[l]**2
            val2 = nums[r]**2
            if val2>=val1:
                res[insertpos]=val2
                r-=1
            else:
                res[insertpos]=val1
                l+=1
            insertpos-=1
        return res

        