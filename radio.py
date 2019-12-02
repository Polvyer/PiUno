import os
from nanpy import Arduino, Lcd

buttonPin = 7
buttonState = 0

Arduino.pinMode(buttonPin, input)

lcd = Lcd([12, 11, 5, 4, 3, 2], [16, 2])

max_trax = 6

# Prints track info to LCD
def getTrack():
   L= [S.strip('\n') for S in os.popen('mpc').readlines()]
   station = L[0][0:15]
   track = L[0][-16:-1]
   lcd.printString(16*" ", 0, 0)
   lcd.printString(station, 0, 0)
   lcd.printString(16*" ", 0, 1)
   lcd.printString(track, 0, 1)
   print L
   print station
   print track

track_num = 1
os.system("mpc play "+str(track_num))
getTrack()

# Event Loop
while True:
   # Get button input
   buttonState = Arduino.digitalRead(buttonPin)
   # Change to next track
   if buttonState:
       track_num += 1
       # After track 6, go back to track 1
       if track_num > max_trax:
           track_num = 1
       os.system("mpc play " + str(track_num))
       getTrack()
   # Do nothing
   else:
       print("Nothing")

"""
   elif key == "LEFT":
      track_num -= 1
      if track_num < 1:
         track_num = 1
      os.system("mpc play " + str(track_num))
      getTrack()
   elif key == "SEL":
      os.system("mpc toggle")
      getTrack()
"""
