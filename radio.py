import os
from nanpy import Arduino, Lcd

# Initialize buttons and states
buttonPin = 7
buttonPin2 = 8
buttonState = 0
buttonState2 = 0

# Activate buttons
Arduino.pinMode(buttonPin, input)
Arduino.pinMode(buttonPin2, input)

# Initialize LCD
lcd = Lcd([12, 11, 5, 4, 3, 2], [16, 2])

# Maximum number of stations held in the mpc list
max_trax = 4

# Print station info to LCD
def getTrack():
   L= [S.strip('\n') for S in os.popen('mpc').readlines()]
   station = L[0][0:15]
   track = L[0][-16:-1]
   lcd.printString(16*" ", 0, 0)
   lcd.printString(station, 0, 0)
   lcd.printString(16*" ", 0, 1)
   lcd.printString(track, 0, 1)
   print (L)
   print (station)
   print (track)

# Play first station and print out station info to the LCD
track_num = 1
os.system("mpc play "+str(track_num))
getTrack()

# Event loop
while True:
   # Get button inputs
   buttonState = Arduino.digitalRead(buttonPin)
   buttonState2 = Arduino.digitalRead(buttonPin2)
   # Change to next station
   if buttonState:
       track_num += 1
       # After track 4, go back to track 1
       if track_num > max_trax:
           track_num = 1
       os.system("mpc play " + str(track_num))
       getTrack()
   # Toggle station
   elif buttonState2:
       os.system("mpc toggle")
       getTrack()
