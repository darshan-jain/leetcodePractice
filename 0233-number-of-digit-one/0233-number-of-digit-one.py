class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0 
        pow10 = 1
        while pow10 <= n :
            divisor = pow10*10 
            quo = n // divisor 
            remainder = n % divisor 

            ans+= quo * pow10 

            if remainder >= pow10:
                ans+=min(remainder - pow10 + 1, pow10)
            pow10*=10
        return ans
        