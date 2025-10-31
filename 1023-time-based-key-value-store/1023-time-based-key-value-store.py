class TimeMap:

    def __init__(self):
        self.ds = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.ds[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.ds or len(self.ds[key])==0:
            return ""
        else:
            l = 0 
            arr = self.ds[key]
            r = len(arr)-1
            res = ""
            while l<=r:
                m = (l+r)//2
                if arr[m][1] <=timestamp:
                    res = arr[m][0]
                    l = m+1
                else:
                    r = m-1
            return res


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)