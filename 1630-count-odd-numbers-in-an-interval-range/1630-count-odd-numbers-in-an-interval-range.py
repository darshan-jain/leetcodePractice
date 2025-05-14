class Solution:
    def countOdds(self, low: int, high: int) -> int:
        numOfEle = high - low +1
        count = numOfEle//2
        if numOfEle%2 and low%2:
            count+=1
        return count

        
        