import cv2
import random
import time
from playsound import playsound

letters = ['A', 'B', 'C', 'D', 'E']

while True:
    #---------------------------
    choice = str(random.randint(1,5))
    a_choice = random.choice(letters)
    t_choice = random.randint(40, 300) #40 Seconds to 5 minutes random interval
    pic = (f"{choice}.jpg")
    sound = str(f"{a_choice}.mp3")
    #---------------------------
    print(pic)

    x = cv2.imread(pic)

    cv2.imshow("Bruh", x)

    if cv2.waitKey(1) &0xFF == ord('q'):
        continue
    
    playsound(sound)

    time.sleep(t_choice)


