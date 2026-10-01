class UndergroundSystem:

    def __init__(self):
        self.data = {}
        self.avg = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.data[id]=(stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        prev = self.data[id]
        tottime = t - prev[1]
        fro= prev[0]
        #del self.data[id]
        to = stationName
        if (fro,to) in self.avg:
            val,cnt = self.avg[(fro,to)]
            val+=tottime
            cnt+=1
            self.avg[(fro,to)] = (val,cnt)
        else:
            self.avg[(fro,to)] = (tottime, 1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        vall = self.avg[(startStation, endStation)]
        return vall[0]/vall[1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)