from playsound import playsound
import random

choices = ['Chichen itza w creepmxne.mp3', 
'GRAVECHILL Twilight.mp3', 
'KUTE AVOID ME.mp3', 
'Sadfriendd x MUPP vendetta.mp3', 
'SHADXWBXRN ARCHEZ KXNVRA PRINCE OF DARKNESS.mp3', 
'SMOKE Cowbell Cult Full Song.mp3']

def play():
    while True:
        playsound('Music\\' + random.choice(choices))

play()