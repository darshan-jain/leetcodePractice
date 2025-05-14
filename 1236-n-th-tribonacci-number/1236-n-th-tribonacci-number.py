class Solution:
    def tribonacci(self, n: int) -> int:
        # if n==0:
        #     return 0
        # if n==1:
        #     return 1
        # if n==2:
        #     return 1 
        # return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

        #dp solution 
        arr = [0,1,1]
        if n<=2:
            return arr[n]
        for i in range(3,n+1):
            arr.append(arr[i-1]+arr[i-2]+arr[i-3])
        return arr[n]

        