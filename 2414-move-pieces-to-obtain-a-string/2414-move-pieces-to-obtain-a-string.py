class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # i =0 
        # j = 0 
        # n = len(start)
        # m = len(target)
        # while i<n or i<m:
        #     while i<n and start[i]=="_":
        #         i+=1
        #     while j<m and target[j]=="_":
        #         j+=1
            
        #     if i==n or j==m:
        #         return i==n and j==m
            
        #     if start[i]!=target[j]:
        #         return False 
        #     if start[i]=="L" and i<j:
        #         return False 
        #     if start[i]=="R" and i>j:
        #         return False
        #     i+=1
        #     j+=1
        
        # return True

        n = len(start)
        result = target
        m = len(result)
        i = 0 
        j = 0 
        while i<n or j<m:
            while i<n and start[i]=='_':
                i+=1
            while j<m and result[j]=='_':
                j+=1
            

            #if end is reached
            
            if i == n or j == m:
                return i == n and j == m
            
            
            if start[i]!=result[j]:
                return False 
            if start[i]=="L" and i<j:
                return False 
            if start[i]=="R" and i>j:
                return False 
            
            i+=1
            j+=1
        return True
        
        