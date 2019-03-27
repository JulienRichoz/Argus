# Microphone Intensity Listen and Record

Argus server use spl_meter_window.py or spl_meter_display.py application to listen and record in database microphone intensity values. All applications are written in python language.

## Install
In order to use spl_meter_window you must install all necessary python dependencies.

### Install Pyaudio

The pyaudio module provides Python binding for PortAudio, the cross-platform I/O library. It is used to read usb microphone data.

To install the Pyaudio module use:

    # apt-get install python-pyaudio python3-pyaudio

>For more informations use the [Official Doc](https://people.csail.mit.edu/hubert/pyaudio/docs/)

### Install NumPy
The NumPy module is a fundamenetal package for scientific computing. It used in this case for decoding streamed values from microphone.

To install the NumPy module use:

    # pip3 install numpy

>For more informations use the [Official Doc](http://www.numpy.org/)

### Install SciPy
The SciPy module allow you to filter a data sequence using a digital filter. It works using for many fundamental data types.

To install the SciPy module use:

    # pip3 install scypy

 >For more informations use the [Official Doc](https://docs.scipy.org/doc/scipy/reference/index.html)

 ### Install MySQLdb

 The MySQLdb module allow you to manage shema db in mysql server. It used in this case to store intensities values into database

 To install MySQLdb module use:

    # pip3 install mysqlclient

 >For more informations use the [Official Doc](http://mysql-python.sourceforge.net/MySQLdb.html)

 ## Other modules
 The others modules included in this project are already installed in your server raspberry. You hove to do nothing.