class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:
            return [i for i in range(n)]
        neighbors = [set() for _ in range(n)]
        for a,b in edges:
            neighbors[a].add(b)
            neighbors[b].add(a)
        
        leaves = []
        for i in range(n):
            if len(neighbors[i])==1:
                leaves.append(i)
        
        remnodes = n 
        while remnodes>2:
            remnodes-=len(leaves)
            temp = []
            for leaf in leaves:
                for neighbor in neighbors[leaf]:
                    neighbors[neighbor].remove(leaf)
                    if len(neighbors[neighbor])==1:
                        temp.append(neighbor)
            leaves = temp
        return leaves


        