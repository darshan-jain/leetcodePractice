class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowf = 0 
        colf = 0 
        rowl = len(matrix)
        coll = len(matrix[0])
        res = []
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0 

        while rowf < rowl and colf < coll:
            for col in range(colf, coll):
                res.append(matrix[row][col])
            rowf+=1

            for row in range(rowf,rowl):
                res.append(matrix[row][col])
            coll-=1

            if rowf <rowl and colf<coll:
                for col in range(coll-1,colf-1,-1):  #-1 since in the last loop the cursor would be at a point extra, hence to offset it
                    res.append(matrix[row][col])
                rowl-=1

                for row in range(rowl-1,rowf-1,-1):
                    res.append(matrix[row][col])
                colf+=1
        return res
        