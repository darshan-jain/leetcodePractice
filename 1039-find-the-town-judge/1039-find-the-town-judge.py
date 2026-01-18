class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        if len(trust)==0:
            return -1
        graph = defaultdict(set)
        for i in range(len(trust)):
            a = trust[i][0]
            b = trust[i][1]
            graph[a].add(b)
        
        judge = -1

        for i in range(1,n+1):
            if i not in graph:
                judge = i 
                break
        
        if judge==-1:
            return -1
        else:
            cnt = 0
            for k,v in graph.items():
                #check i in all v
                if judge in v:
                    cnt+=1
            
            return judge if cnt==n-1 else -1


        