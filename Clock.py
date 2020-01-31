from Messenger import *

class Clock():
    
    HourCount = 5
    MinuteCount = 59
    DayCount = 1

    def ReturnTime(self):
        if (self.MinuteCount < 10):    
            return str(self.HourCount) + ":0" + str(self.MinuteCount) + str(", Day ") + str(self.DayCount)
        else:
            return str(self.HourCount) + ":" + str(self.MinuteCount) + str(", Day ") + str(self.DayCount)

    def Tick(self):
        
        self.MinuteCount += 1

        if (self.MinuteCount >= 60):
            self.MinuteCount = 0
            self.HourCount += 1

        if (self.HourCount >= 24):
            self.HourCount = 0
            self.DayCount += 1

        if (self.HourCount == 6 and self.MinuteCount == 0):
            for i in TheMessenger.ListOfPeople:
                TheMessenger.ToMessenger("TheClock", i.Name, "Wake Up", "Now", "NULL")

        elif (self.HourCount == 22 and self.MinuteCount == 0):
            for i in TheMessenger.ListOfPeople:
                TheMessenger.ToMessenger("TheClock", i.Name, "Go To Bed", "Now", "NULL")