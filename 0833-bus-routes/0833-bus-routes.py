from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0 
        
        graph = defaultdict(list)
        for i,route in enumerate(routes):
            for stop in route:
                graph[stop].append(i)
        
        q = deque([(source, 0)]) #stop, number of buses taken so far 
        visited_stops = {source}
        visited_buses = set()
        while q:
            stop, buses_taken = q.popleft()
            for bus in graph[stop]:
                if bus in visited_buses:
                    continue
                visited_buses.add(bus)

                for next_stop in routes[bus]:
                    if next_stop == target:
                        return buses_taken+1
                    if next_stop not in visited_stops:
                        visited_stops.add(next_stop)
                        q.append((next_stop, buses_taken+1))
        return -1

        