class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        cnt = 0 
        for num in nums:
            if len(str(num))%2==0:
                cnt+=1
        return cnt
        