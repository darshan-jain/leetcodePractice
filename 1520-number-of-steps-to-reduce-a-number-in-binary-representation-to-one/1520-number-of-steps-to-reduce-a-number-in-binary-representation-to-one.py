class Solution:
    def numSteps(self, s: str) -> int:

        dec = int(s,2)
        times = 0 
        while dec!=1:
            if dec%2==1:
                dec+=1
                
            else:
                dec//=2
            times+=1
        return times


        