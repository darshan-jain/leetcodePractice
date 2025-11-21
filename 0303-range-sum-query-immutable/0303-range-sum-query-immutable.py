class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        for i,num in enumerate(nums):
            if i==0:
                self.prefix.append(num)
            else:
                self.prefix.append(self.prefix[-1]+num)
                

    def sumRange(self, left: int, right: int) -> int:
        leftSum = self.prefix[left-1] if left>0 else 0 
        rightSum = self.prefix[right]
        return rightSum-leftSum
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


#optimised approach would be to actually store the prefix sum so that left sum and right sum can be got individually 
# rightSum = self.prefix[right]
# leftSum = self.prefix[left-1] if left>0 else 0 
# return rightSum - leftSum
