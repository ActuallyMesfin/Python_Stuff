#THE WHOLE OF POINT OF THIS IS SIMPLY TO PUT RANDOM JUMPSCARES
#BECAUSE WHY THE HELL NOT, EH?
#⚠️I DOWNLOADED THE DOWNGRADED VERSION OF PLAYSOUND LIBRARY FROM PIP
#⚠️DUE TO AN ERROR THAT KEPT POPPING UP (MIS OR SOMETHING)
#USE THIS: pip uninstall playsound AND THEN pip install playsound==1.2.2 IF YOU DOWNLOADED
#THE LATEST VERSION



#---------------------------------IMPORTS
import cv2
import random
import time
from playsound import playsound 
#---------------------------------IMPORTS

letters = ['A', 'B', 'C', 'D', 'E']

while True:
    #---------------------------
    choice = ('Images\\' + str(random.randint(1,5)))
    a_choice = ('Audio\\' + random.choice(letters))
    t_choice = random.randint(40, 300) 
    pic = (f"{choice}.jpg")
    sound = str(f"{a_choice}.mp3")
    #---------------------------
    print(pic)

    x = cv2.imread(pic)

    cv2.imshow("Bruh", x)

    cv2.waitKey(1)
    
    playsound(sound)
    cv2.destroyAllWindows()
    time.sleep(t_choice)


