from graphics import *
import time
import keyboard
import playsound
playsound.playsound('music.mp3', False) # YES STACKOVERFLOW
w = GraphWin("Get The CPU!™ 2", 960, 720)
EpicList = []
Thing = Image(Point(30,30), "Thing.gif")
thingX = 30
thingY = 30
EpicList.append(Thing)
Thing.draw(w)
while True: # Movement
    if keyboard.is_pressed('D') == True:
        if thingX <= 960:
            thingX = thingX + 8
            Thing = Image(Point(thingX, thingY), "Thing.gif")
            Thing.draw(w)
            EpicList[0].undraw()
            del EpicList[0]
            EpicList.append(Thing)
    if keyboard.is_pressed('A') == True:
        if thingX >= 0:
            thingX = thingX - 8
            Thing = Image(Point(thingX, thingY), "Thing.gif")
            Thing.draw(w)
            EpicList[0].undraw()
            del EpicList[0]
            EpicList.append(Thing)
    if keyboard.is_pressed('W') == True:
        if thingY >= 0:
            thingY = thingY - 8
            Thing = Image(Point(thingX, thingY), "Thing.gif")
            Thing.draw(w)
            EpicList[0].undraw()
            del EpicList[0]
            EpicList.append(Thing)
    if keyboard.is_pressed('S') == True:
        if thingY <= 720:
            thingY = thingY + 8
            Thing = Image(Point(thingX, thingY), "Thing.gif")
            Thing.draw(w)
            EpicList[0].undraw()
            del EpicList[0]
            EpicList.append(Thing)