class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0 
        r = rows*cols-1
        while l<=r:
            m = (l+r)//2
            val = matrix[m//cols][m%cols] #cols since we are explanding on the cols axis
            if val==target:
                return True
            elif val > target:
                r= m-1
            else:
                l = m+1
        return False


        