class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix), len(matrix[0])

        for row in range(rows):
            if matrix[row][-1] >=  target:
                rowFlag = row
                break
            if matrix[-1][-1] < target:
                return False
        
        #do binary search in that row
        left = 0 
        right = len(matrix[0])
        while left<= right:
            mid = (left+right)//2
            if matrix[rowFlag][mid] == target:
                return True
            elif matrix[rowFlag][mid] > target:
                right = mid-1
            else:
                left = mid+1
        
        return False
        