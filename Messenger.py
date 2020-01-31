class Message:
	def __init__(self, theSender, theReceiver, theMessage, theTimestamp, theExtraInfo):
		self.sender = theSender
		self.receiver = theReceiver
		self.message = theMessage
		self.timestamp = theTimestamp
		self.extraInfo = theExtraInfo

	sender = ""
	receiver = ""
	message = ""
	timestamp = ""
	extraInfo = ""

	def Thing(self):
		print(self.sender)


class Messenger(object):
	_instance = None
	def __new__(class_, *args, **kwargs):
		if not isinstance(class_._instance, class_):
			class_._instance = object.__new__(class_, *args, **kwargs)
		return class_._instance

	Display_Width = 1000
	Display_Height = 600

	ListOfPeople = []
	ListOfLocations = [
		["Office", (Display_Width / 2), 50, 50, 50, (0, 0, 0)],
		["Store", (Display_Width / 2), 250, 50, 50, (0, 0, 0)],
		["Pub", (Display_Width / 2), 450, 50, 50, (0, 0, 0)],
		["Part Time Work", (Display_Width - 100), 150, 50, 50, (0, 0, 0)]
					]


	def ToMessenger(self, sender, receiver, message, timestamp, extraInfo):
		if (timestamp == "Now"):
			self.ToPerson(sender, receiver, message, extraInfo)



	def ToPerson(self, sender, receiver, message, extraInfo):
		for i in self.ListOfPeople:
			if (i.Name == receiver):
				i.ReceiveMessage(sender, receiver, message, extraInfo)
				break


TheMessenger = Messenger()