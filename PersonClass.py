from States import *
from Messenger import *
import random

class Person:
	def __init__(self, theName, HouseXLocation, HouseYLocation):
		self.Name = theName
		self.CurrentLocation = theName + "'s House"
		self.xCoordinate = HouseXLocation
		self.yCoordinate = HouseYLocation

		self.HungerMultiplier = random.uniform(0.8, 1.2)
		self.ThirstMultiplier = random.uniform(0.8, 1.2)
		self.SleepMultiplier = random.uniform(0.8, 1.2)
		self.SocialMultiplier = random.uniform(0.8, 1.2)
		self.MoneyMultiplier = random.uniform(0.6, 1.7)
		self.Meals = random.randrange(5, 16, 1)

		self.Color = []
		self.Color.append(random.randrange(0, 256, 1))
		self.Color.append(random.randrange(0, 256, 1))
		self.Color.append(random.randrange(0, 256, 1))

		TheMessenger.ListOfPeople.append(self)
		TheMessenger.ListOfLocations.append([self.CurrentLocation, HouseXLocation, HouseYLocation, 20, 20, (0, 200, 255)])

	Name = "Name"
	Hunger = 100.0
	Thirst = 100.0
	Sleep = 100.0
	Social = 100.0
	Money = 0.0
	Meals = 5
	Bullets = 0

	HungerMultiplier = 1.0
	ThirstMultiplier = 1.0
	SleepMultiplier = 1.0
	SocialMultiplier = 1.0
	MoneyMultiplier = 1.0

	CurrentState = Sleeping()
	PreviousState = Idle()
	CurrentLocation = "Location"
	NeedToShop = False
	WantToSocialize = False
	GoingOutTonight = False

	xCoordinate = 50
	yCoordinate = 250
	MovementSpeed = 10.0
	Height = 10
	Width = 10
	#Color = [255, 0, 0]
	Color = 0

	def Die():
		for person in TheMessenger.SocialPeople:
			if(person == self.Name):
				TheMessenger.SocialPeople.remove(person)
				for i in TheMessenger.SocialPeople:
					TheMessenger.ToMessenger(self.Name, i, "Not Going Out", "Now", "NULL")
				break
		for person in TheMessenger.CurrentlySocializing:
			if(person == self.Name):
				TheMessenger.CurrentlySocializing.remove(person)
				for i in TheMessenger.CurrentlySocializing:
					TheMessenger.ToMessenger(self.Name, i, "Not Going Out", "Now", "NULL")
				break
		for index, person in enumerate(TheMessenger.ListOfPeople):
			if(person.Name == self.Name):
				TheMessenger.ListOfPeople.pop(index)
				break


	def CalculateTimeToLeave(self, Hour, Minute, DestinationCoordinateX, DestinationCoordinateY):
		Distance = abs(DestinationCoordinateX - self.xCoordinate)
		if (Distance < abs(DestinationCoordinateY - self.yCoordinate)):
			Distance = abs(DestinationCoordinateY - self.yCoordinate)

		Distance = int(Distance/self.MovementSpeed)

		while (Distance > 60):
			Hour -= 1
			Distance -= 60
			if (Hour < 0):
				Hour += 24

		Minute -= Distance
		if (Minute < 0):
			Minute += 60
			Hour -= 1

		if (Minute < 10):    
			return (str(Hour) + ":0" + str(Minute))
		else:
			return (str(Hour) + ":" + str(Minute))

	def CancelGoingOut(self):

		if (self.CurrentState.StateName == "Socializing"):
			self.WantToSocialize = False
			self.GoingOutTonight = False
			TheMessenger.CurrentlySocializing.remove(self.Name)

			if (len(TheMessenger.CurrentlySocializing) > 0):
					print(self.Name + " says: I think I'm heading home for today. Goodnight!")
			else:
				print(self.Name + " says: I guess I might as well head home too then.")

			for i in TheMessenger.CurrentlySocializing:
					TheMessenger.ToMessenger(self.Name, i, "Not Going Out", "Now", "NULL")

		else:
			if(self.WantToSocialize):
				self.WantToSocialize = False
				TheMessenger.SocialPeople.remove(self.Name)
			if(self.GoingOutTonight):
				self.GoingOutTonight = False
				print(self.Name + " says: Sorry, I won't make it to the pub tonight afterall.")
				for i in TheMessenger.SocialPeople:
					TheMessenger.ToMessenger(self.Name, i, "Not Going Out", "Now", "NULL")


	def StandardUpdate(self):
		if (self.Hunger > 100.0):
			self.Hunger = 100.0

		if (self.Thirst > 100.0):
			self.Thirst = 100.0

		if (self.Sleep > 100.0):
			self.Sleep = 100.0

		if (self.Social > 100.0):
			self.Social = 100.0

		if (self.Thirst < 50.0 and self.CurrentState.StateName != "Traveling" and self.CurrentState.StateName != "Drinking" and self.CurrentState.StateName != "Eating" and self.CurrentState.StateName != "Socializing"):
			if (self.CurrentState.StateName != "Sleeping" or self.Thirst < 20.0):
				TheMessenger.ToMessenger(self.Name, self.Name, "Finish Drinking", 5, "NULL")
				self.PreviousState = self.CurrentState
				self.CurrentState = Drinking()

		if (self.Sleep < 20.0 and self.CurrentState.StateName == "Sleeping"):
			if (self.CurrentLocation == (self.Name + "'s House")):
				self.CurrentState = Sleeping()
			else:
				TheMessenger.ToMessenger(self.Name, self.Name, "Go Home", "Now", "Sleep")

		if (self.Social < 70.0 and self.Money > 50.0 and self.NeedToShop == False and self.WantToSocialize == False and (self.CurrentState.StateName == "Working" or self.CurrentState.StateName == "Idle")):
			self.WantToSocialize = True
			TheMessenger.ToMessenger(self.Name, "Messenger", "Want To Socialize", "Now", "NULL")
			if (len(TheMessenger.SocialPeople) == 1):
				print(self.Name + " says: I wanna go out to drink. Anyone up for it?")
			elif (len(TheMessenger.SocialPeople) == 2):
				print(self.Name + " says: I'm planning on going out too " + TheMessenger.SocialPeople[0] + ". Let's hang out!")
				TheMessenger.ToMessenger(self.Name, TheMessenger.SocialPeople[0], "Let's Hang Out", "Now", "NULL")
			else:
				print(self.Name + " says: I think I'll join you guys at the pub.")
			if (len(TheMessenger.SocialPeople) > 1):
				self.GoingOutTonight = True
				#TheMessenger.ToMessenger(self.Name, self.Name, "Go", "18:00", [TheMessenger.ListOfLocations[2][1], TheMessenger.ListOfLocations[2][2], "Pub"])

		
		if (self.Hunger <= 0.0):
			print(self.Name, "died from hunger.")
			self.Die()

		elif (self.Thirst <= 0.0):
			print(self.Name, "died from thirst.")
			self.Die()

		elif (self.Sleep <= 0.0):
			print(self.Name, "died from exhaustion.")
			self.Die()

		elif (self.Social <= 0.0):
			print(self.Name, "committed suicide out of lonelyness.")
			self.Die()


	def ReceiveMessage(self, sender, receiver, message, extraInfo):
		if (message == "Wake Up" and sender == "TheClock" and self.CurrentLocation == (self.Name + "'s House")):
			if (self.CurrentState.StateName == "Drinking"):
				self.PreviousState = Idle()
			else:
				self.CurrentState = Idle()
			TheMessenger.ToMessenger(self.Name, self.Name, "Eat Food", "6:30", "NULL")
			if (self.Money > 200 and self.Bullets > 0):
				TimeToLeave = self.CalculateTimeToLeave(8, 0, TheMessenger.ListOfLocations[3][1], TheMessenger.ListOfLocations[3][2])
				TheMessenger.ToMessenger(self.Name, self.Name, "Go", TimeToLeave, [TheMessenger.ListOfLocations[3][1], TheMessenger.ListOfLocations[3][2], "Forest"])
			else:
				TimeToLeave = self.CalculateTimeToLeave(8, 0, TheMessenger.ListOfLocations[0][1], TheMessenger.ListOfLocations[0][2])
				TheMessenger.ToMessenger(self.Name, self.Name, "Go", TimeToLeave, [TheMessenger.ListOfLocations[0][1], TheMessenger.ListOfLocations[0][2], "Office"])

			if (self.Meals < 5):
				print(self.Name + " needs to go shopping.")
				self.NeedToShop = True
				self.CancelGoingOut()

		elif (message == "Eat Food" and self.Meals > 0 and self.CurrentState.StateName != "Sleeping"):
			if (self.CurrentLocation == (self.Name + "'s House") or self.CurrentLocation == "Office" or self.CurrentLocation == "Forest"):
				TheMessenger.ToMessenger(self.Name, self.Name, "Finish Eating", 30, "NULL")
				self.Meals -= 1
				if (self.CurrentState.StateName != "Drinking"):
					self.PreviousState = self.CurrentState
				self.CurrentState = Eating()

			elif (self.CurrentLocation == "On The Road" or self.CurrentLocation == "Store"):
				TheMessenger.ToMessenger(self.Name, self.Name, "Eat Food", 30, "NULL")

		elif (message == "Finish Eating" and sender == self.Name and self.CurrentState.StateName == "Eating"):
			self.CurrentState = self.PreviousState

		elif (message == "Finish Drinking" and sender == self.Name and self.CurrentState.StateName == "Drinking"):
			self.CurrentState = self.PreviousState

		elif (message == "Go" and sender == self.Name):
			self.CurrentState = Traveling((extraInfo[0] - self.xCoordinate), (extraInfo[1] - self.yCoordinate), extraInfo[2], "NULL")
			self.CurrentLocation = "On The Road"

		elif (message == "Go Home" and sender == self.Name and self.CurrentLocation != (self.Name + "'s House")):
			self.CancelGoingOut()
			for i in TheMessenger.ListOfLocations:
					if (i[0] == (self.Name + "'s House")):
						self.CurrentState = Traveling((i[1] - self.xCoordinate), (i[2] - self.yCoordinate), i[0], extraInfo)
						self.CurrentLocation = "On The Road"
						break

		elif (message == "Arrive At Location" and sender == self.Name):
			self.CurrentLocation = extraInfo[0]

			if (extraInfo[0] == "Office" or extraInfo[0] == "Forest"):
				self.CurrentState = Working()

			elif (extraInfo[0] == "Store"):
				self.NeedToShop = False
				self.CurrentState = Shopping(extraInfo[1])

			elif (extraInfo[0] == "Pub"):
				self.CurrentState = Socializing()
				TheMessenger.SocialPeople.remove(self.Name)
				TheMessenger.CurrentlySocializing.append(self.Name)

			elif (extraInfo[0] == (self.Name + "'s House")):
				if (extraInfo[1] == "Sleep"):
					self.CurrentState = Sleep()
				else:
					self.CurrentState = Idle()

		elif (message == "Leave Work" and sender == "TheClock" and self.CurrentState.StateName == "Working"):

			if (self.GoingOutTonight):
				TimeToLeave = self.CalculateTimeToLeave(18, 0, TheMessenger.ListOfLocations[2][1], TheMessenger.ListOfLocations[2][2])
				TheMessenger.ToMessenger(self.Name, self.Name, "Go", TimeToLeave, [TheMessenger.ListOfLocations[2][1], TheMessenger.ListOfLocations[2][2], "Pub"])

			elif (self.NeedToShop or (self.Money > 300 and self.Bullets < 20)):
				BulletTime = "NULL"
				if (self.Money > 300 and self.Bullets < 20):
					BulletTime = "Bullets"	
				self.CurrentState = Traveling((TheMessenger.ListOfLocations[1][1] - self.xCoordinate), (TheMessenger.ListOfLocations[1][2] - self.yCoordinate), "Store" , BulletTime)
				self.CurrentLocation = "On The Road"

			else:
				TheMessenger.ToMessenger(self.Name, self.Name, "Go Home", "Now", "NULL")

		elif (message == "Go To Bed"):
			if (self.CurrentLocation == (self.Name + "'s House")):
				self.CurrentState = Sleeping()
			else:
				TheMessenger.ToMessenger(self.Name, self.Name, "Go To Bed", 60, "NULL")

			if (self.CurrentState.StateName == "Socializing"):
				TheMessenger.ToMessenger(self.Name, self.Name, "Go Home", "0:00", "NULL")

		elif (message == "Let's Hang Out"):
			self.GoingOutTonight = True
			#TheMessenger.ToMessenger(self.Name, self.Name, "Go", "17:30", [TheMessenger.ListOfLocations[2][1], TheMessenger.ListOfLocations[2][2], "Pub"])
			print(self.Name + " says: Sure thing " + TheMessenger.SocialPeople[1] + "!")

		elif (message == "Not Going Out"):
			if (self.CurrentState.StateName == "Socializing" and len(TheMessenger.CurrentlySocializing) < 2):
				TheMessenger.ToMessenger(self.Name, self.Name, "Go Home", "Now", "NULL")
			elif (len(TheMessenger.SocialPeople) < 2):
				self.GoingOutTonight = False