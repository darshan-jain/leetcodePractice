import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t = Counter(tasks)
        maxheap = []
        for k,v in t.items():
            heapq.heappush(maxheap, (-v,k))
        
        q = deque()
        time = 0 
        while maxheap or q:
            time+=1
            if maxheap:
                freq,task = heapq.heappop(maxheap)
                if freq+1<0:
                    q.append((time+n, task, freq+1))
            if q and time >= q[0][0]:
                qtime, qtask, qfreq = q.popleft()
                heapq.heappush(maxheap,(qfreq,qtask))
        return time

        