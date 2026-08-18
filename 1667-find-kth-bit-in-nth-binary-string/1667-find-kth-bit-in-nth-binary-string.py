class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        inversion_count = 0
        
        while n > 1:
            length = (1 << n) - 1
            mid = (length // 2) + 1
            
            if k == mid:
                # Middle bit is "1". Invert if inversion_count is odd.
                return "0" if inversion_count % 2 == 1 else "1"
            
            if k > mid:
                # Mirror k to the left side and track the inversion
                k = length - k + 1
                inversion_count += 1
            
            # Reduce problem size to S_{n-1}
            n -= 1
        
        # Base case S_1 is always "0". 
        # Apply accumulated inversions.
        return "1" if inversion_count % 2 == 1 else "0"