class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack = ["/"]
        # i = 0 

        # l = len(path)-1
        # while l>=0 and path[l]=='/':
        #     l-=1
         
        # while i<len(path):
        #     #remove last slash

        #     if i==len(path)-1 and path[i]=='/':
        #         break
            
        #     while i<len(path) and path[i]=='/':
        #         i+=1
            
        #     j=i
        #     while j<len(path) and path[j]!='/':
        #         j+=1
        #     dirname = path[i:j]
        #     print(dirname)
        #     if dirname == ".":
        #         i=j
        #         continue
        #     elif dirname =="..":
        #         if len(stack)==1:
        #             i=j
        #             continue
        #         else:
        #             if stack[-1]=='/':
        #                 stack.pop()
        #             stack.pop()
        #     elif dirname=="" or dirname=="/": #multiple slashes condition
        #         stack.append('/')
        #     else: #valid dirname
        #         stack.append(dirname)
        #         if j<l:
        #             stack.append('/')
        #     i=j
        
        # while len(stack)>1 and stack[-1]=='/':
        #     stack.pop()
        # return "".join(stack)

        stack = []
        path_items = path.split('/')

        for item in path_items:
            if item=='.' or not item:
                continue
            elif item=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)
        return "/" + "/".join(stack)


        