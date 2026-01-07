class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        elem1 = float("-inf")
        elem2 = float("-inf")
        cnt1 = 0 
        cnt2 = 0 
        n = len(nums)
        for i in range(len(nums)):
            if cnt1==0 and elem2!=nums[i]:
                cnt1 = 1 
                elem1 = nums[i]
            elif cnt2==0 and elem1!=nums[i]:
                cnt2 = 1 
                elem2 = nums[i]
            elif elem1==nums[i]:
                cnt1+=1
            elif elem2==nums[i]:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        ans = []
        cnt1 = 0 
        cnt2 = 0 
        for i in range(len(nums)):
            if nums[i]==elem1:
                cnt1+=1
            if nums[i]==elem2:
                cnt2+=1
        target = (n//3)
        if cnt1 > target:
            ans.append(elem1)
        if cnt2>target:
            ans.append(elem2)
        return ans

        