class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        i=1
        while k>0:
            if i in arr:
                i+=1
            else:
                k-=1
                i+=1
        return i-1

        