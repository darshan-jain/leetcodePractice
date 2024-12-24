from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.res = deque()
        
        

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        
        self.res.append(t)
        range = [t-3000,t]
        while self.res[0] < range[0]:
            self.res.popleft()
        return len(self.res)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)