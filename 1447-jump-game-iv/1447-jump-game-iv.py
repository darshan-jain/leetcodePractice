class Solution:
    def minJumps(self, arr: List[int]) -> int:
        g = defaultdict(list)
        for i,num in enumerate(arr):
            g[num].append(i)
        q = deque([(0,0)])
        visit = set()
        while True:
            idx, dist = q.popleft()
            if idx == len(arr)-1:
                return dist
            if idx in visit:
                continue
            visit.add(idx)
            for j in (idx-1, idx+1, *g.pop(arr[idx],[])):
                if 0<=j<len(arr) and j not in visit:
                    q.append((j ,dist+1))
        return -1
        