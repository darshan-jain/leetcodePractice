class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        rows = len(mat)
        cols = len(mat[0])
        copy = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                copy[i][j]=mat[i][j]
        k = k%cols

        def reverse(arr):
            l = 0 
            r = len(arr)-1 
            while l<=r:
                arr[l],arr[r] = arr[r],arr[l]
                l+=1
                r-=1
        
            return arr
        
        def rotateleft(arr,k):
            
            arr[:k] = reverse(arr[:k])
            arr[k:]  = reverse(arr[k:])
            arr = reverse(arr)
            
            return arr
        
        def rotateright(arr,k):
            nk = len(arr)-k
            arr[:nk] = reverse(arr[:nk])
            arr[nk:] = reverse(arr[nk:])
            arr = reverse(arr)
            
            return arr
        
        for i in range(0,rows,2):
            row = mat[i]
            mat[i] = rotateleft(row, k)
            
        for i in range(1,rows,2):
            row = mat[i]
            mat[i] = rotateright(row,k)
        return mat==copy


            
        