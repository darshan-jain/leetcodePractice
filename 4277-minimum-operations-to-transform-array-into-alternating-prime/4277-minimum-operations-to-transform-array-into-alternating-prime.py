class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = 0 

        def isPrime(val):
            limit = ceil(sqrt(val))
            if val<=1:
                return False
            if val==2:
                return True
            for i in range(2,limit+1):
                if val%i==0:
                    return False 
            return True

        for i,num in enumerate(nums):
            if i%2==0:
                #make sure it is prime 
                while not isPrime(nums[i]):
                    nums[i]+=1
                    res+=1
            
            else:
                #make sure it is non-prime
                while isPrime(nums[i]):
                    nums[i]+=1
                    res+=1
        print(nums)
        return res
        