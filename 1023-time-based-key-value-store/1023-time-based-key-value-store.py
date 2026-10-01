class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value, timestamp))
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm:
            return ""
        lst = self.hm[key]
        if len(lst)==0:
            return ""
        res = ""
        l = 0 
        r = len(lst)-1
        while l<=r:
            m = (l+r)//2
            if lst[m][1]<=timestamp:
                res = lst[m][0]
                l=m+1
            else:
                r = m-1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)