class State:

    def Update(self, ThePerson):
        ThePerson.Hunger -= 1
        #print(ThePerson.Name, "'s Hunger: ", ThePerson.Hunger, sep='')

    HungerStandardLossValue = 0.0625
    ThirstStandardLossValue = 0.0625
    SleepStandardLossValue = 0.035
    SocialStandardLossValue = 1.0


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
        ThePerson.Hunger += 5.0
        ThePerson.Thirst += 5.0
        ThePerson.Sleep -= self.SleepStandardLossValue
        ThePerson.Social -= self.SocialStandardLossValue
        ThePerson.StandardUpdate()
        #print(ThePerson.Name, "'s Thirst: ", ThePerson.Thirst, sep='')



class Drinking(State):

    StateName = "Drinking"
    
    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue
        ThePerson.Thirst = 100
        ThePerson.Sleep -= self.SleepStandardLossValue
        ThePerson.Social -= self.SocialStandardLossValue
        ThePerson.StandardUpdate()

class Sleeping(State):

    StateName = "Sleeping"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue
        ThePerson.Thirst -= self.ThirstStandardLossValue
        ThePerson.Sleep += 0.09
        ThePerson.Social -= self.SocialStandardLossValue
        ThePerson.StandardUpdate()

class Socializing(State):

    StateName = "Socializing"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue
        ThePerson.Thirst -= self.ThirstStandardLossValue
        ThePerson.Sleep -= self.SleepStandardLossValue
        ThePerson.Social += 1.0
        ThePerson.StandardUpdate()

class Working(State):

    StateName = "Working"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue
        ThePerson.Thirst -= self.ThirstStandardLossValue
        ThePerson.Sleep -= self.SleepStandardLossValue * 2
        ThePerson.Social -= self.SocialStandardLossValue
        ThePerson.Money += 1
        ThePerson.StandardUpdate()

class Shopping(State):

    StateName = "Shopping"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue
        ThePerson.Thirst -= self.ThirstStandardLossValue
        ThePerson.Sleep -= self.SleepStandardLossValue
        ThePerson.Social -= self.SocialStandardLossValue
        ThePerson.StandardUpdate()


class Traveling(State):

    StateName = "Traveling"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue
        ThePerson.Thirst -= self.ThirstStandardLossValue
        ThePerson.Sleep -= self.SleepStandardLossValue
        ThePerson.Social -= self.SocialStandardLossValue
        ThePerson.StandardUpdate()


class Idle(State):

    StateName = "Idle"

    def Update(self, ThePerson):
        ThePerson.Hunger -= self.HungerStandardLossValue
        ThePerson.Thirst -= self.ThirstStandardLossValue
        ThePerson.Sleep -= self.SleepStandardLossValue
        ThePerson.Social -= self.SocialStandardLossValue
        ThePerson.StandardUpdate()
        #print(ThePerson.Name, "'s Thirst: ", ThePerson.Thirst, sep='')