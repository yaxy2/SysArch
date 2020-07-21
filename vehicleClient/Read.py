#!/usr/bin/env python

import RPi.GPIO as GPIO
from MFRC522.MFRC522 import *
import signal

continue_reading = True


# function to read uid an conver it to a string

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = format(i, '02X') + mystring
    return mystring


# Capture SIGINT for cleanup when the script is aborted
def end_read(signal, frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522()

# Welcome message
print("Welcome to the MFRC522 data read example")
print("Press Ctrl-C to stop.")

# This loop keeps checking for chips.
# If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards
    (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")

        # Get the UID of the card
        (status, uid) = MIFAREReader.MFRC522_Anticoll()
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            print("Card read UID: %s" % uidToString(uid))
        else:
            print("Authentication error")
