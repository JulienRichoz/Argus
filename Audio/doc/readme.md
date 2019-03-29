# Microphone Read and Store Intensity
Argus projet allow you to get intensities values in decibel form usb micropohone. All values are stored into a database named argus into the audio table. The database used is mysql server

## How to use
The are differentes modules that allow you to read intensity values from usb microphone. You can use:

- spl_meter_display.py
- spl_meter_window.py
- pcm_meter_display.py

### The spl_meter_display
The spl_meter_display.py allow you to read and store in real time(every second) the microphone intensity values in Decibel unit. It also display output values in the terminal. All values are each second stored into a database using mysql.

To use the spl_meter_display.py open a new window terminal and insert:

    # cd /home/pi/Argus/Audio
    # python3 spl_meter_display.py

### The spl_meter_window
The spl_meter_window allow you to read and store in real time(every second) the microphone intensity values in Decibel unit. It also display output values using a window interface in which you can iterate to start and stop recordind values. 

To use the spl_meter_window.py open a new window terminal and insert:

    # cd /home/pi/Argus/Audio
    # python3 spl_meter_window.py

### The pcm_meter_display
The pcm_meter_display is a beta version. It use ALSA pcm capture instead streaming from pyaudio. All intensities values are not stored in database. 

>It a beta version so be careful when using.

To use the pcm_meter_display open a new window terminal and insert:

    # cd /home/pi/Argus/Audio
    # python3 pcm_meter_window.py

## How to install

To use the application you must follow the install proceudre using this link

[Audio Install Procedure](install.md)
