class Solution:
    def countOdds(self, low: int, high: int) -> int:
        num = high - low+1
        cnt = num//2
        if num%2 and low%2:
            cnt+=1
        return cnt
        