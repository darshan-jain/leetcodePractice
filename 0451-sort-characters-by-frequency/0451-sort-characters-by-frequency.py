import heapq
class Solution:
    def frequencySort(self, s: str) -> str:
        hm = Counter(s)
        heap = [(-count,char) for char,count in hm.items()]
        heapq.heapify(heap)
        res = []
        while heap:
            freq,letter  = heapq.heappop(heap)
            freq *=-1
            for i in range(freq):
                res.append(letter)
        return "".join(res)

        