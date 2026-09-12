class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        r = len(boxGrid)
        c = len(boxGrid[0])
        new = [["."]*r for _ in range(c)]

        def transform(ar):
            n = len(ar)
            insert = n-1
            i=n-1
            while i>=0:
                # if it is empty 
                if ar[i]==".":
                    i-=1
                #if it is a stone 
                elif ar[i]=="#":
                    ar[insert], ar[i] = ar[i], ar[insert]
                    i-=1
                    insert-=1

                # if it is a stationary object
                else:
                    i-=1
                    insert = i 
            return ar


        for i,row in enumerate(boxGrid):
            arr = transform(row)
            print(arr)
            for j in range(len(arr)):
                new[j][r-1-i] = arr[j]
        return new
        