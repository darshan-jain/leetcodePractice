class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src,dest in sorted(tickets)[::-1]:
            graph[src].append(dest)
        
        stack = ["JFK"]
        itenary = []

        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            itenary.append(stack.pop())
        return list(reversed(itenary))

        