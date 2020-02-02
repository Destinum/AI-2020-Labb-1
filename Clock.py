from Messenger import *

class Clock():
    
    HourCount = 5
    MinuteCount = 50
    DayCount = 1
    TimeString = "5:50"

    def ReturnTime(self):
        return self.TimeString + ", Day " + str(self.DayCount)

    def CalculateTimeStamp(self, time):
        Minutes = self.MinuteCount + time
        Hours = self.HourCount
        while (Minutes >= 60):
            Hours += 1
            Minutes -= 60
        while (Hours >= 24):
            Hours -= 24

        if (Minutes < 10):    
            return (str(Hours) + ":0" + str(Minutes))
        else:
            return (str(Hours) + ":" + str(Minutes))

    def Tick(self):
        
        self.MinuteCount += 1

        if (self.MinuteCount >= 60):
            self.MinuteCount = 0
            self.HourCount += 1

        if (self.HourCount >= 24):
            self.HourCount = 0
            self.DayCount += 1

        if (self.MinuteCount < 10):    
            self.TimeString = str(self.HourCount) + ":0" + str(self.MinuteCount)
        else:
            self.TimeString = str(self.HourCount) + ":" + str(self.MinuteCount)

        if (self.TimeString == "6:00"):
            for i in TheMessenger.ListOfPeople:
                TheMessenger.ToMessenger("TheClock", i.Name, "Wake Up", "Now", "NULL")

        elif (self.TimeString == "12:00"):
            for i in TheMessenger.ListOfPeople:
                TheMessenger.ToMessenger("TheClock", i.Name, "Eat Food", "Now", "NULL")

        elif (self.TimeString == "17:00"):
            for i in TheMessenger.ListOfPeople:
                TheMessenger.ToMessenger("TheClock", i.Name, "Leave Work", "Now", "NULL")

        elif (self.TimeString == "18:00"):
            for i in TheMessenger.ListOfPeople:
                TheMessenger.ToMessenger("TheClock", i.Name, "Eat Food", "Now", "NULL")

        elif (self.TimeString == "22:00"):
            for i in TheMessenger.ListOfPeople:
                TheMessenger.ToMessenger("TheClock", i.Name, "Go To Bed", "Now", "NULL")

        IndexesToDelete = []
        for index, message in enumerate(TheMessenger.DelayedMessages):
            if(isinstance(message.timestamp, int)):
                TheMessenger.DelayedMessages[index].timestamp = self.CalculateTimeStamp(message.timestamp)
            if(message.timestamp == self.TimeString):
                TheMessenger.ToMessenger(message.sender, message.receiver, message.message, "Now", message.extraInfo)
                IndexesToDelete.insert(0, index)
        for index in IndexesToDelete:
            TheMessenger.DelayedMessages.pop(index)