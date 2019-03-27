# spl_meter_window
# show intensity mic in Db and store values in databse
# Carboni Davide
# v1.0

import tkinter as tk
import  tkinter.font
import os, errno
import pyaudio
import spl_lib as spl
from scipy.signal import lfilter
import numpy
import time
from storeData import StoreDB

''' The following is similar to a basic CD quality
   When CHUNK size is 4096 it routinely throws an IOError.
   When it is set to 8192 it doesn't.
   IOError happens due to the small CHUNK size

   What is CHUNK? Let's say CHUNK = 4096
   math.pow(2, 12) => RATE / CHUNK = 100ms = 0.1 sec
'''
CHUNKS = [4096, 9600]       # Use what you need
CHUNK = CHUNKS[1]
FORMAT = pyaudio.paInt16    # 16 bit
CHANNEL = 1    # 1 means mono. If stereo, put 2

'''
Different mics have different rates.
For example, Logitech HD 720p has rate 48000Hz
'''
RATES = [44100, 48000]
RATE = RATES[1]

NUMERATOR, DENOMINATOR = spl.A_weighting(RATE)
'''
Listen to mic
'''
pa = pyaudio.PyAudio()
store = StoreDB()
canStore = False

# audio stream
stream = pa.open(format = FORMAT,
                channels = CHANNEL,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)

#program exit
def exit():
    win.quit()

def listen(lableIntensity, lableRecording):

    global canStore

    def getIntensity():

        global canStore

        try:
            ## read() returns string. You need to decode it into an array later.
            block = stream.read(CHUNK,  exception_on_overflow = False)
        except IOError as e:
            lableIntensity.config(" (%d) Error recording: %s" % (e))
            lableIntensity.after(100, new_decibel)
        else:
            ## Int16 is a numpy data type which is Integer (-32768 to 32767)
            ## If you put Int8 or Int32, the result numbers will be ridiculous
            decoded_block = numpy.fromstring(block, 'Int16')
            ## This is where you apply A-weighted filter
            y = lfilter(NUMERATOR, DENOMINATOR, decoded_block)
            new_decibel = 20*numpy.log10(spl.rms_flat(y))
            print(canStore)
            if canStore:
                store.store(new_decibel)

            lableIntensity.config(text='A-weighted: {:+.2f} dB'.format(new_decibel))
            lableIntensity.after(1000, getIntensity)            

    # get next intensity value
    getIntensity()
    return
            
def update_btn_text():

    global canStore
    global buttonText
    global lableRecording

    # change recording status
    if canStore:
        buttonText.set("Start Record")
        lableRecording.config(text="")
        canStore = False
    else:
        buttonText.set("Stop Record")
        lableRecording.config(text="Recording...")
        canStore = True
    return

# define a new winodows
win = tk.Tk()
# define window title
win.title("Sound Intensity")
# define a personal font 
myFont = tkinter.font.Font(family='Helvetica', size = 42, weight = "bold")
# Define static window (no resize)
win.resizable(width=False, height=False)
#define windows size
win.geometry("400x200")

#show intensity
lableIntensity = tk.Label(win)
lableIntensity.config(font=("Helvetica", 26))
lableIntensity.place(x=35, y=50)

#show recording status
lableRecording = tk.Label(win)
lableRecording.config(font=("Helvetica", 10))
lableRecording.place(x=35, y=100)

# activate or desactivate recording data to Db
buttonText = tk.StringVar()
button = tk.Button(win, textvariable=buttonText, width=25, command=update_btn_text)
buttonText.set("Start Record")
button.place(x=85, y=150)

# use the listen to get intensity in real time
listen(lableIntensity, lableRecording)

# open windows and listen intensity
tk.mainloop()

#close streaming
stream.stop_stream()
stream.close()
pa.terminate()