class UndergroundSystem:

    def __init__(self):
        self.travelInfo={}
        self.timeInterval={}    
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.travelInfo[id]=(stationName,t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        inistationName,checkin_time=self.travelInfo.pop(id)
        travel_time=t-checkin_time
        tupleForKey=(inistationName,stationName)
        if tupleForKey in self.timeInterval:
            prevTime,count=self.timeInterval[tupleForKey]
            self.timeInterval[tupleForKey]=prevTime+travel_time,count+1
        else:
            self.timeInterval[tupleForKey]=travel_time,1

        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        checkTuple=(startStation,endStation)
        total_time,count=self.timeInterval[checkTuple]
        return total_time/count
