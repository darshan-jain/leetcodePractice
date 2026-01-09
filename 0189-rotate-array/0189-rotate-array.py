class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(nums,s,e):
            while e>s:
                nums[s],nums[e] = nums[e],nums[s]
                s+=1
                e-=1
            return nums
        n = len(nums)
        k = k%n
        nums = rev(nums, 0, n-1)
        nums = rev(nums, 0,k-1)
        nums = rev(nums, k,n-1)
        