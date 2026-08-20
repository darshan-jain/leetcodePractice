class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        ans = 0 
        hist = [0]*len(matrix[0])

        for row in matrix:
            for i,val in enumerate(row):
                hist[i] = 0 if val ==0 else hist[i]+1
            
            sortedhist = sorted(hist)

            for i,h in enumerate(sortedhist):
                ans = max(ans, h*(len(row)-i))
        
        return ans

        