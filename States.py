from Messenger import *
import random

class State:

    def Update(self, ThePerson):
        ThePerson.Hunger -= 1
        #print(ThePerson.Name, "'s Hunger: ", ThePerson.Hunger, sep='')

    HungerStandardLossValue = 0.0625
    ThirstStandardLossValue = 0.2
    SleepStandardLossValue = 0.035
    SocialStandardLossValue = 0.02


"""
    Hunger = 100.0
	Thirst = 100.0
	Sleep = 100.0
	Social = 100.0
	Money = 0.0
	Meals = 5
"""


#class ChangeState(State):


class Eating(State):

    StateName = "Eating"

    def Update(self, ThePerson):
        ThePerson.Hunger += 2.0
        ThePerson.Thirst += 2.0
        ThePerson.Sleep -= self.SleepStandardLossValue * ThePerson.SleepMultiplier
        ThePerson.Social -= self.SocialStandardLossValue * ThePerson.SocialMultiplier
        ThePerson.StandardUpdate()
        #print(ThePerson.Name, "'s Thirst: ", ThePerson.Thirst, sep='')



class Drinking(State):

    StateName = "Drinking"
    
    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue * ThePerson.HungerMultiplier
        ThePerson.Thirst += 20.0
        ThePerson.Sleep -= self.SleepStandardLossValue * ThePerson.SleepMultiplier
        ThePerson.Social -= self.SocialStandardLossValue * ThePerson.SocialMultiplier
        ThePerson.StandardUpdate()

class Sleeping(State):

    StateName = "Sleeping"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue * ThePerson.HungerMultiplier * 0.5
        ThePerson.Thirst -= self.ThirstStandardLossValue * ThePerson.ThirstMultiplier * 0.6
        ThePerson.Sleep += 0.095
        ThePerson.Social -= self.SocialStandardLossValue * ThePerson.SocialMultiplier
        ThePerson.StandardUpdate()

class Socializing(State):

    StateName = "Socializing"
    Food = 0
    Drink = 0

    def Update(self, ThePerson):
        if (ThePerson.Thirst < 70.0 and ThePerson.Money > 20 and self.Drink <= 0):
            self.Drink = 20
            ThePerson.Money -= 20
        
        if (ThePerson.Hunger < 70.0 and ThePerson.Money > 30 and self.Food <= 0):
            self.Food = 30
            ThePerson.Money -= 30

        if (self.Drink > 0):
            self.Drink -= 1
            ThePerson.Thirst += 2.0
        else:
            ThePerson.Thirst -= self.ThirstStandardLossValue * ThePerson.ThirstMultiplier

        if (self.Food > 0):
            self.Food -= 1
            ThePerson.Hunger += 2.0
        else:
            ThePerson.Hunger -= self.HungerStandardLossValue * ThePerson.HungerMultiplier

        ThePerson.Sleep -= self.SleepStandardLossValue * ThePerson.SleepMultiplier
        ThePerson.Social += 0.2
        ThePerson.Money -= 0.1
        ThePerson.StandardUpdate()

        if(ThePerson.Social >= 100 or ThePerson.Money < 1.0):
            TheMessenger.ToMessenger(ThePerson.Name, ThePerson.Name, "Go Home", "Now", "NULL")

class Working(State):

    StateName = "Working"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue * ThePerson.HungerMultiplier * 1.5
        ThePerson.Thirst -= self.ThirstStandardLossValue * ThePerson.ThirstMultiplier * 1.5
        ThePerson.Sleep -= self.SleepStandardLossValue * ThePerson.SleepMultiplier * 1.5
        ThePerson.Social -= self.SocialStandardLossValue * ThePerson.SocialMultiplier * 0.5

        if (ThePerson.CurrentLocation == "Office"):
            ThePerson.Money += 0.2 * ThePerson.MoneyMultiplier
        elif (ThePerson.CurrentLocation == "Forest" and ThePerson.Bullets > 0):
            FoundMoose = random.randrange(1, 201, 1)
            if (FoundMoose == 1):
                ThePerson.Bullets -= random.randrange(1, 6, 1)
                if (ThePerson.Bullets < 0):
                    ThePerson.Bullets = 0
                KilledMoose = random.randrange(1, 5, 1)
                if (KilledMoose == 1):
                    print(ThePerson.Name + " found a moose and managed to kill it!")
                    print(ThePerson.Name + " received 200 money for the moose.")
                    ThePerson.Money += 200
                else:
                    print(ThePerson.Name + " found a moose, but failed to kill it.")

        ThePerson.StandardUpdate()

class Shopping(State):
    def __init__(self, extraInfo):
        if (extraInfo == "Bullets"):
            self.BulletTime = True

    StateName = "Shopping"
    BuyThisFrame = False
    BulletTime = False

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue * ThePerson.HungerMultiplier
        ThePerson.Thirst -= self.ThirstStandardLossValue * ThePerson.ThirstMultiplier
        ThePerson.Sleep -= self.SleepStandardLossValue * ThePerson.SleepMultiplier
        ThePerson.Social -= self.SocialStandardLossValue * ThePerson.SocialMultiplier

        if (self.BulletTime and self.BuyThisFrame and ThePerson.Bullets < 20):
            ThePerson.Bullets += 1
            ThePerson.Money -= 10
            if (ThePerson.Money < 100):
                self.BulletTime = False

        if (ThePerson.Meals < 15 and ThePerson.Money >= 10 and self.BuyThisFrame):
            ThePerson.Meals += 1
            ThePerson.Money -= 10
        elif ((ThePerson.Meals >= 15 or ThePerson.Money < 10) and (self.BulletTime == False or ThePerson.Bullets >= 20)):
            TheMessenger.ToMessenger(ThePerson.Name, ThePerson.Name, "Go Home", "Now", "NULL")

        self.BuyThisFrame = not self.BuyThisFrame
        ThePerson.StandardUpdate()


class Traveling(State):
    def __init__(self, TheDistanceX, TheDistanceY, destination, extraInfo):
        self.ExtraInfo = extraInfo
        self.Destination = destination
        self.DistanceX = TheDistanceX
        self.DistanceY = TheDistanceY
        
        if (TheDistanceX < 0.0):
            self.DistanceX = - TheDistanceX
            self.DirectionX = - 1.0

        if (TheDistanceY < 0.0):
            self.DistanceY = - TheDistanceY
            self.DirectionY = - 1.0

    StateName = "Traveling"
    Destination = "Default"
    DistanceX = 0.0
    DistanceY = 0.0
    DirectionX = 1.0
    DirectionY = 1.0
    ExtraInfo = "NULL"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue * ThePerson.HungerMultiplier
        ThePerson.Thirst -= self.ThirstStandardLossValue * ThePerson.ThirstMultiplier
        ThePerson.Sleep -= self.SleepStandardLossValue * ThePerson.SleepMultiplier
        ThePerson.Social -= self.SocialStandardLossValue * ThePerson.SocialMultiplier

        if (self.DistanceX > 0.0):
            ThePerson.xCoordinate += (ThePerson.MovementSpeed * self.DirectionX)
            self.DistanceX -= ThePerson.MovementSpeed
            if (self.DistanceX < 0.0):
                ThePerson.xCoordinate -= (self.DistanceX * self.DirectionX)

        if (self.DistanceY > 0.0):
            ThePerson.yCoordinate += (ThePerson.MovementSpeed * self.DirectionY)
            self.DistanceY -= ThePerson.MovementSpeed
            if (self.DistanceY < 0.0):
                ThePerson.yCoordinate -= (self.DistanceY * self.DirectionY)

        elif (self.DistanceX <= 0.0 and self.DistanceY <= 0.0):
            TheMessenger.ToMessenger(ThePerson.Name, ThePerson.Name, "Arrive At Location", "Now", [self.Destination, self.ExtraInfo])

        ThePerson.StandardUpdate()


class Idle(State):

    StateName = "Idle"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue * ThePerson.HungerMultiplier
        ThePerson.Thirst -= self.ThirstStandardLossValue * ThePerson.ThirstMultiplier
        ThePerson.Sleep -= self.SleepStandardLossValue * ThePerson.SleepMultiplier
        ThePerson.Social -= self.SocialStandardLossValue * ThePerson.SocialMultiplier
        ThePerson.StandardUpdate()
        #print(ThePerson.Name, "'s Thirst: ", ThePerson.Thirst, sep='')