class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        low = 0 
        high = n-1
        while low<high:
            mid = (low+high)//2
            if matrix[mid][-1]>=target:
                high = mid
            else:
                low = mid+1
        

        #low row has the element
        l = 0
        r = m-1
        while l<=r:
            m = (l+r)//2
            if matrix[low][m]==target:
                return True
            elif matrix[low][m]>target:
                r = m-1
            else:
                l = m+1
        
        return False
        