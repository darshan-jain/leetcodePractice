class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr)<=1:
            return True
        diff = arr[1]-arr[0]
        for i in range(len(arr)-1):
            x = arr[i]
            y = arr[i+1]
            if y-x!=diff:
                return False 
        return True
        