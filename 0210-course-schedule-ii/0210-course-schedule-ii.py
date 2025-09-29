from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)
        
        seen = set()
        flag = 0 
        
        def cycle(course,seen):
            if course in seen:
                return True
            seen.add(course)
            for c in graph[course]:
                if cycle(c,seen):
                    return True
            seen.remove(course)
            graph[course] = []
            return False

        
        for i in range(numCourses):
            if cycle(i,seen):
                flag=1 # not possible
        
        if flag==1:
            return []

        #findorder 

        adj = defaultdict(list)
        st = []

        for a,b in prerequisites:
            adj[b].append(a)
        vis = [0 for _ in range(numCourses)]
        
        def dfs(node,vis,adj,st):
            vis[node]=1
            for nei in adj[node]:
                if vis[nei]!=1:
                    dfs(nei, vis,adj,st)
            st.append(node)

        
        for i in range(numCourses):
            if vis[i]!=1:
                dfs(i,vis,adj,st)
        
        ts = []
        while st:
            ts.append(st.pop())
        return ts


        