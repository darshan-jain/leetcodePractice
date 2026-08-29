class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((timestamp,value))
        

    def get(self, key: str, timestamp: int) -> str:
        lst = self.hm[key]
        l = 0 
        r = len(lst)-1
        resWord = ""
        while l<=r:
            m = (l+r)//2
            if lst[m][0] <= timestamp:
                resWord = lst[m][1]
                l = m+1
            else:
                r=m-1
        return resWord
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)