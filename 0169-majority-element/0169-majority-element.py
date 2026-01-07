class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element = None 
        cnt = 0 
        for num in nums:
            if cnt==0:
                element = num
            if element ==num:
                cnt+=1
            else:
                cnt-=1
        return element
        