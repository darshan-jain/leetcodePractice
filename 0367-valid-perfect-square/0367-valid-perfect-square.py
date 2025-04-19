class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        high = num / 2
        high = math.ceil(high)
        low = 1
        while low <=high:
            mid = low + ((high-low)//2)
            if mid*mid == num:
                return True
            elif mid*mid > num:
                high = mid-1
            else:
                low = mid+1
        return False

        