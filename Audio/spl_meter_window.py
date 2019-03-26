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
canStore = True

# audio stream
stream = pa.open(format = FORMAT,
                channels = CHANNEL,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK)

# button text to active o desactivate store in Db
buttonText = tk.StringVar()

#program exit
def exit():
    win.quit()

def listen(label):
    
    def getIntensity():

        try:
            ## read() returns string. You need to decode it into an array later.
            block = stream.read(CHUNK,  exception_on_overflow = False)
        except IOError as e:
            label.config(" (%d) Error recording: %s" % (e))
            label.after(100, new_decibel)
        else:
            ## Int16 is a numpy data type which is Integer (-32768 to 32767)
            ## If you put Int8 or Int32, the result numbers will be ridiculous
            decoded_block = numpy.fromstring(block, 'Int16')
            ## This is where you apply A-weighted filter
            y = lfilter(NUMERATOR, DENOMINATOR, decoded_block)
            new_decibel = 20*numpy.log10(spl.rms_flat(y))
            if canStore:
                store.store(new_decibel)
            label.config(text='A-weighted: {:+.2f} dB'.format(new_decibel))
            label.after(1000, getIntensity)

    # get next intensity value
    getIntensity()
            
def update_btn_text():
    if canStore:
        buttonText = "Stop Record"
        canStore = False
    else:
        buttonText = "Start Record"
        canStore = True


# define a new winodows
win = tk.Tk()
# define window title
win.title("Sound Intensity")
# define a personal font 
myFont = tkinter.font.Font(family='Helvetica', size = 22, weight = "bold")
# Define static window (no resize)
win.resizable(width=False, height=False)
#define windows size
win.geometry("400x300")
#show title in window
label = tk.Label(win)
label.config(fontsize="20")
label.pack()

# use the listen to get intensity in real time
listen(label)
label.place(x=150, y=50)

# activate or desactivate recording data to Db
button = tk.Button(win, textvariable=buttonText, width=25, command=update_btn_text)
button.pack()

# open windows and listen intensity
tk.mainloop()

#close streaming
stream.stop_stream()
stream.close()
pa.terminate()