class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        def helper(arr):
            for i in range(1, len(arr)):
                if i==1:
                    arr[i] = max(arr[i], arr[i-1])
                else:
                    arr[i] = max(arr[i] + arr[i-2], arr[i-1])
            if len(arr)>1 and  arr[-2]:
                return max(arr[-1], arr[-2])
            else:
                return arr[-1]
        return max(helper(nums[1:]), helper(nums[:-1]))
        