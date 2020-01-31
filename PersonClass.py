from States import *
from Messenger import *

class Person:
	def __init__(self, theName, HouseXLocation, HouseYLocation):
		self.Name = theName
		self.CurrentLocation = theName + "'s House"
		TheMessenger.ListOfPeople.append(self)
		TheMessenger.ListOfLocations.append([self.CurrentLocation, HouseXLocation, HouseYLocation, 20, 20, (0, 200, 255)])
	
	Name = "Name"
	Hunger = 100.0
	Thirst = 100.0
	Sleep = 100.0
	Social = 100.0
	Money = 0.0
	Meals = 5

	CurrentState = Sleeping()
	CurrentLocation = "Location"

	xCoordinate = 50
	yCoordinate = 250
	Height = 10
	Width = 10
	Color = [255, 0, 0]

	#MessengerReference = Messenger()

	def StandardUpdate(self):
		if (self.Hunger > 100.0):
			self.Hunger = 100.0

		if (self.Thirst > 100.0):
			self.Thirst = 100.0

		if (self.Sleep > 100.0):
			self.Sleep = 100.0

		if (self.Social > 100.0):
			self.Social = 100.0


		#if (self.Hunger <= 90.0 and self.Name == "Steve"):
		"""if (self.Hunger <= 0.0):
			TheMessenger.ListOfPeople.pop(0)
			#TheMessenger.ListOfPeople.remove('Steve')
			print(self.Name, "died from hunger.")

		elif (self.Thirst <= 0.0):
			TheMessenger.ListOfPeople.pop(0)
			print(self.Name, "died from thirst.")"""

		if (self.Sleep <= 0.0):
			TheMessenger.ListOfPeople.pop(0)
			print(self.Name, "died from exhaustion.")

		#elif (self.Social <= 0.0):
			#TheMessenger.ListOfPeople.pop(0)
			#print(self.Name, "committed suicide out of lonelyness.")


	def ReceiveMessage(self, sender, receiver, message, extraInfo):
		if (message == "Wake Up" and sender == "TheClock"):
			self.CurrentState = Idle()
			self.xCoordinate = TheMessenger.ListOfLocations[0][1]
			self.yCoordinate = TheMessenger.ListOfLocations[0][2]

		elif (message == "Go To Bed" and sender == "TheClock"):
			self.CurrentState = Sleeping()

			for i in TheMessenger.ListOfLocations:
				if (i[0] == (self.Name + "'s House")):
					self.xCoordinate = i[1]
					self.yCoordinate = i[2]
					break
