class Solution:

    def helper(self, arr, i,sum1, sum2,sum3,sum4,target):
        if sum1>target or sum2>target or sum3>target or sum4>target:
            return False
        if i==-1:
            if sum1==sum2==sum3==sum4==target:
                return True
            else:
                return False
        return self.helper(arr, i-1,sum1+arr[i], sum2,sum3,sum4,target) or self.helper(arr, i-1,sum1, sum2+ arr[i],sum3,sum4,target) or self.helper(arr, i-1,sum1, sum2,sum3 + arr[i],sum4,target) or self.helper(arr, i-1,sum1, sum2,sum3,sum4 + arr[i],target)
        
    def makesquare(self, matchsticks: List[int]) -> bool:
        tot = sum(matchsticks)
        target = tot/4
        if tot%4!=0:
            return False 
        
        matchsticks.sort()
        sum1 = sum2 = sum3 = sum4 = 0 
        return self.helper(matchsticks,len(matchsticks)-1,sum1,sum2,sum3,sum4,target)

        