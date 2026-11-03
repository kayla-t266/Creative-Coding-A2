# Import Micro:bit functions
from microbit import *

# Import music
import music

# Import built-in sounds
import audio


# SONG 1: Twinkle Twinkle Little Star

def twinkle():

        # First line
    music.play([
        "C4:4", "C4:4", "G4:8", "G4:8",
        "A4:4", "A4:4", "G4:8",

        # Second line
        "F4:4", "F4:4", "E4:4", "E4:4",
        "D4:4", "D4:4", "C4:8",

        # Third line
        "G4:4", "G4:4", "F4:4", "F4:4",
        "E4:4", "E4:4", "D4:8",

        # Fourth line
        "G4:4", "G4:4", "F4:4", "F4:4",
        "E4:4", "E4:4", "D4:8",

        # Fifth line
        "C4:4", "C4:4", "G4:8", "G4:8",
        "A4:4", "A4:4", "G4:8",

        # Sixth line
        "F4:4", "F4:4", "E4:4", "E4:4",
        "D4:4", "D4:4", "C4:8"
    ])


# SONG 2: Baa Baa Black Sheep

def baa_baa():

        # First line
    music.play([
        "C4:4", "C4:4", "G4:4", "G4:4",
        "A4:4", "B4:4", "C5:8", "A4:4", "G4:8",

        # Second line
        "F4:4", "F4:4", "F4:4", "F4:4",
        "E4:4", "E4:4", "E4:4", "E4:4",
        "D4:4", "D4:4", "D4:4", "D4:4", "C4:8",

        # Third line
        "G4:4", "G4:4", "G4:4",
        "F4:4", "F4:4", "F4:4",
        "E4:4", "E4:4", "E4:4", "D4:8",

        # Fourth line 
        "G4:4", "G4:4", "G4:4",
        "F4:4", "F4:4", "F4:4",
        "E4:4", "E4:4", "E4:4", "D4:8",

        # Fifth line
        "C4:4", "C4:4", "G4:4", "G4:4",
        "A4:4", "B4:4", "C5:8", "A4:4", "G4:8",

        # Sixth line
        "F4:4", "F4:4", "F4:4", "F4:4",
        "E4:4", "E4:4", "E4:4", "E4:4",
        "D4:4", "D4:4", "D4:4", "D4:4", "C4:8"
    ])


# Giggle when shaken

def giggle():
    audio.play(Sound.GIGGLE)


# Set up the buttons

# Make both pins read high when not pressed
pin0.set_pull(pin0.PULL_UP)
pin1.set_pull(pin1.PULL_UP)

# Display a heart when program begins
display.show(Image.HEART)

while True:

    # Shake to play the giggle sound
    if accelerometer.was_gesture("shake"):
        giggle()
        display.show(Image.HEART)

    # Button 1: P0 plays Twinkle Twinkle
    if pin0.read_digital() == 0:
        twinkle()

        # Wait until button 1 is released
        while pin0.read_digital() == 0:
            sleep(10)

        display.show(Image.HEART)

    # Button 2: P1 plays Baa Baa Black Sheep
    elif pin1.read_digital() == 0:
        baa_baa()

        # Wait until button 2 is released
        while pin1.read_digital() == 0:
            sleep(10)

        display.show(Image.HEART)
        
    sleep(50)


        
