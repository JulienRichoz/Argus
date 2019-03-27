# Argus

Argus is a python project to get and store into database informations from camera and usb microphone.

## How it work

...to do

### Video

### Audio
The audio application allow you to read the intensity values in real time from the usb microphone.

### Store data
To store all captured informations the server use the RDBMS mariaDb server. The shema is called argus. The audio table is used to store decibel intensity every second, while video table is used to store counted people par second.

## Techinical informations and Install procedure

[Audio Technical documentation](./Audio/doc/readme.md)

## Access Information

### Raspberry

pi user:
- user name: pi
- password: raspberry

root user:

- user name: root
- password: argus

### MariaDb connection

root user:

- user name: root
- password: root
- access right from: anywhere

### Samba Connection

pi user:

- user name: pi
- password: raspberry
- folder: \Argus

