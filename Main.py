import pygame
import time
from Messenger import *
from Clock import Clock
from PersonClass import Person
from States import *

pygame.init()
Window = pygame.display.set_mode((TheMessenger.Display_Width, TheMessenger.Display_Height))
pygame.display.set_caption("AI Labb")

def text_object(text, font):
    textSurface = font.render(text, True, (0, 0, 0))
    return textSurface, textSurface.get_rect()


Timer = Clock()
LastTime = time.process_time()
CurrentTime = time.process_time()

Person("Necko", 900, 400)
Person("Ron", 700, 400)
Person("Becky", 900, 500)
Person("Ben", 700, 500)
Person("Margarit", 300, 400)
Person("Stank", 300, 500)
Person("El Kexet", 500, 700)

TheTime = ""

smallTextSize = 10

largeText = pygame.font.Font('freesansbold.ttf', 20)
smallText = pygame.font.Font('freesansbold.ttf', smallTextSize)

#Tingy = [["Fisk", "Stuff"], ["Fisk2", "Stuff2"]]
#print(Tingy[1][1])

Paused = False
UpdateRate = 0.01
Running = True
while Running:

    CurrentTime = time.process_time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
            break
        
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_SPACE):
                Paused = not Paused
            if (event.key == pygame.K_KP_ENTER):
                try:
                    val = float(input("Enter new update rate per second: "))
                    UpdateRate = 1.0 / val
                except ValueError:
                    print("Couldn't convert input to usable value.")
            if (event.key == pygame.K_ESCAPE):
                Running = False
                break


    if (Paused == False and (CurrentTime - LastTime) >= UpdateRate):
        
        Window.fill((255, 255, 255))

        Timer.Tick()
        TheTime = Timer.ReturnTime()
        LastTime = CurrentTime

        TextSurf, TextRect = text_object(TheTime, largeText)
        TextRect.topright = (TheMessenger.Display_Width - 10, 10)
        Window.blit(TextSurf, TextRect)


        if (len(TheMessenger.ListOfPeople) == 0):
            break

        for k in TheMessenger.ListOfLocations:
            pygame.draw.rect(Window, k[5], ((k[1] - k[3] / 2), (k[2] - k[4] / 2), k[3], k[4]))
            
            TextSurf, TextRect = text_object(k[0], smallText)
            TextRect.midtop = (k[1], (k[2] + k[4] / 2))
            Window.blit(TextSurf, TextRect)


        LineSpace = smallTextSize
        for i in TheMessenger.ListOfPeople:
            i.CurrentState.Update(i)
            pygame.draw.rect(Window, (i.Color[0], i.Color[1], i.Color[2]), ((i.xCoordinate - i.Width / 2), (i.yCoordinate - i.Height / 2), i.Width, i.Height))

            CharacterStats = [(str(i.Name) + "'s Current State: " + str(i.CurrentState.StateName)),
                                (str(i.Name) + "'s Current Location: " + str(i.CurrentLocation)),
                                (str(i.Name) + "'s Hunger: " + str(i.Hunger)),
                                (str(i.Name) + "'s Thirst: " + str(i.Thirst)),
                                (str(i.Name) + "'s Sleep: " + str(i.Sleep)),
                                (str(i.Name) + "'s Social: " + str(i.Social)),
                                (str(i.Name) + "'s Money: " + str(i.Money)),
                                (str(i.Name) + "'s Meals Remaining: " + str(i.Meals)),
                                (str(i.Name) + "'s Bullets Remaining: " + str(i.Bullets)),
                                (" ")]

            pygame.draw.rect(Window, (i.Color[0], i.Color[1], i.Color[2]), (10, (LineSpace - smallTextSize), i.Width, i.Height))
            for Text in CharacterStats:
                TextSurf, TextRect = text_object(Text, smallText)
                TextRect.topleft = (10, LineSpace)
                Window.blit(TextSurf, TextRect)
                LineSpace += smallTextSize


    pygame.display.update()

pygame.quit()
print("Session ended at " + TheTime)