class UndergroundSystem:
    
    def __init__(self):
      self.checkInMap = {} # id -> (startStation, checkInTime)
      self.totalMap = {} # (start, end) -> [totalTime, count] not tuple, because it's immutable

    def checkIn(self, id: int, startStation: str, checkInTime: int) -> None:
      self.checkInMap[id] = (startStation, checkInTime)
        
    def checkOut(self, id: int, endStation: str, checkOutTime: int) -> None:
      startStation, checkInTime = self.checkInMap[id]

      route = (startStation, endStation)
      if route not in self.totalMap:
        self.totalMap[route] = [0, 0] # initialize route

      self.totalMap[route][0] += checkOutTime - checkInTime # increment totalTime
      self.totalMap[route][1] += 1 # increment count
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
      totalTime, count = self.totalMap[(startStation, endStation)]
      return totalTime / count # not double slashes 

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)