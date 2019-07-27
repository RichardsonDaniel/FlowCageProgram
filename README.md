


 <p align="center">
  <img src="http://richardsondaniel.co.uk/KidsApp/img/english/animals/mouse.png"/>
</p>


#  <p align="center"> Anemotaxis Chamber</p>

<p align="center">"Program to record, time and operate the anemotaxis chamber designed for the lab -  developed for IISER (Indian Institutes of Science Education and Research)"</p>

# 


This program is the basis for the Anemotaxis chamber within the lab, the program is used to control recording, water delivery and port sensing during trails. When operating the program gets defined inputs from the user per trail, on trail start the Pi begins recording throught the connected Pi camera and loops through constantly checking each of the four sample ports. When it detects a presence within the port from the connected IR sensors it will either record the time and port number as a failed port check or record and begin water delivery if the port is the correct sample port ending the trial. Water delivery is handled by a connected 8 channel relay which opens a water valve for the predefined timings, the recording and CSV values are then exported.

## Files:

[](https://emojipedia.org/file-folder/)
##### - 📁OUTPUT
###### This folder will be populated with the CSV sheet with timings/port output file and two video files pers session, on .H264 and one converted .MP4
[](https://emojipedia.org/page-facing-up/)
##### - 📄 FlowCageProgram
###### Python file designed to be run on the raspberry pi in the lab to contol a touchscreen, camera, a set of 8 relays and a bank of IR emmiters/recievers.
[](https://emojipedia.org/page-facing-up/)
##### - 📄 README.txt
###### ReadME is the document you are currently reading holding usage and general information.



### Dependencies: 
The source code on this project is meant to be run on the installed Raspberry Pi on the Anemotaxis chamber, if you require this for your own purpose you will have to repurpose the pin list IN and OUT arrays for your setup, currently pins;

21, 20, 16, 26, 19, 13, 6, 5

are used for outputs to the 8 channel relay, ordered correctly 1 through 8. The pins;

12, 1, 0, 8

are used as input pins from the bank of 4 IR emitters/recievers and are positioned across the 4 flow ports. The rest of the pins (including the 5v power rails) are assigned to the touchscreen.

## How to use:

#### Input fields:
##### - Mouse number input field:
Use this field to give the Mouse a corresponding name, this name will be recorded onto the video file produced and in the CSV file for identification later.
##### - Number of ports in use dropdown:
Use this dropdown to indicate how many ports you are going to use for your trial, between 1 and 4 sample ports.
##### - Correct port number drop down: 
Use this dropdown to choose the port which the program will use as the correct port, when this port is sampled by the mouse the trial will end and water will be delivered.
##### - Delivery time in seconds drop down: 
Use this drop down to determine how long water should be delivered into the correct sample port after it has been sampled by the mouse, the timings are in seconds and range from 0.1s (100ms) to 2s (2000ms)
##### - Radio choice between begin Trial and Test ports for 10s: 
There are two radio choice buttons, they will let you choose what happens when the "Begin" button is pressed. "begin trial" option starts a standard trial using the parameters you have set. "Test ports for 10s" make it so each sample port will set off each of the corresponding relay channels for 10 seconds, this is a quick and easy way to test and troubleshoot sample ports.
 
#### Buttons:
##### - Begin:
Begin starts the program and runs the decided radio option, either the standard trial script or the test ports script.
##### - Get Num:
Get Num will read the number of ports you currently want to use and will ask you how many of each port number you need, it will then give you a 3 times randomised list of all the port numbers you need. For example if you want to use 3 ports and need to run 4 trials you could be given a list such as; 123312231312.
##### - Flip Cam: 
Flips cam will flip the feed from the camera vertically, after being chosen this will be the default camera position for the remaining trials and will be the orientation in the recording.
##### - Test Cam: 
Test cam will show a live feed from the camera on the display for 5 seconds, useful for correctly orientating and testing. This does not display on a connected phone or computer it will only display on the connected touch screen display.
##### - Test LED: 
Test LED will test all the LED indicators and relay channels on the relay board, it will cycle through all the channels 1-8 to test them individually, then fire off in set bunches to test if there is enough power to run them all.
##### - Save & Exit: 
Save & Exit will close and save the CSV file currently being used, cleanup the output voltage to the pins of the relay and IR sensors and close the program. The CSV file whilst open can and will save periodically however it is important that you DO NOT EXIT WITHOUT PRESSING SAVE & EXIT if you simply press the close button in the top right your file may be in the process of being used and be corrupted, always close the progam with the "Save & Exit" button.

#### Output:
##### - CSV File: 
Each time the program is opened a new CSV file is created in the "OUTPUT" folder and given the time and date as a name, each time a trail is ran the number of the animal and all the timings are recorded this file is saved and closed upon exiting the program by the "Save & Exit" this allows mutiple trials in one sesson to be written to one file if the program is left open.
##### - Video Files: 
The camera records raw to .H264 and this file is created into the "OUTPUT" folder, its name is made of the number of the mouse used and the time the trial was ran. This file type is not suitable for most post processing as such a copy is automatically converted into .MP4, therefore  each trail should have two video created in the "OUTPUT" folder after each run.
 
### How to run a trail start to finish: 
1)
2)
3)
4)
5)
6)
### Connecting to Phone/Computer :


## How it works:

### Program and basics: 

### Relay Module: 

### IR Module and sensors: 

### Pi Camera Module: 

### Valves and Wiring/Tubing: 

## Troubleshooting/FAQ:

**If this section is not helping you with your problem there are  individual test in the "Test Scripts" folder on the desktop, each part of the program (camera, relay, IR Beams & logic) can all be tested individually to sort out your issues.**

### IR Beam: 
##### •   Relay is not firing after beam broken:  
Check if the beam is actually being broken, on the main red board there are four lights one for each sample port. These lights will be constantly on until something comes in close proximity check to make sure these lights go out, if they dont then there is a connection issue between the IR beam and the board, if they do then the problem is with the relay.
##### •   Too much/few sensitivity: 
On the main red board next to the blue relay there are four screw points connecting to the four IR sensors, these screw points can be turned left and right and will adjust the sensetivity of each beam independently.
##### •   Channel 4 is not peforming: 
Channel 4 operates differently it will not show movement, unlike the other 3 which can be tested as soon as the Pi boots up, until it has been activated by the program. Once the program boots up channel 4 will perform the same as the other channels

### Water: 
##### •   Water is not being delivered: 
##### •   Too much/few water is being delivered: 

### Camera: 
##### •   pi.camera error:  
##### •   no image feed: 
 
### Relay: 
##### •   Relay channel not clicking on: 
If the LED indicator turns on but the relay  does not "click" or start water flow then the relay is not getting enough power, it requires 5vDC to operate. The jumper wire (black running from JVCC to VCC) could also have become loose. 
##### •   Only some channels working: 
The relay is not getting enough power, it requires 5vDC to operate.
##### •   Led indicators sticking on: 
This happens when the Pi did not get to run a cleanup of pins on last operation, it will not effect any trials but if you are concerned press the "Test LED" button it will run a cleanup on completion

### Program: 
##### •   Will not open: 
If you are running from the .sh file on the desktop the pi will sometimes refuse to open this way if permissions are not set or are invalidated, open the flowcage program folder and open the .py file, this will open in a program called thorny, press the big green button to manually open the program.
##### •   Timings need changing: 
There are many points in the program where timing could be added, removed or changed. If for instance you wanted to add a delay before delivery simply add time.sleep("time you want in s") just before delivery. Same for any other timings look for the appropriate position and add this line or edit it if it already exists.
##### •   Files not appearing/empty CSV file: 
If the CSV file is empty or missing content you did enot properly shutdown on last run, you must press the "Save & Exit" button to ensure all your data is saved correctly. If the .MP4 file is missing for a praticular video but the .H264 remais the Pi was not given enough time between trials to convert the file. You will have to manually convert it.

## Pi desktop image with dependencies:

Rasberry pi with preinstalled libraries source code and setups [LINK].

## Parts used:

#####    Raspberry Pi 3 B+: 
###### [Amazon Link](https://www.amazon.in/gp/product/B07CWVSMLS/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
#####    8 Channel 5v Relay: 
######  [Amazon Link](https://www.amazon.in/gp/product/B01IDNCCFQ/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)
#####    Raspberry pi v2 camera: 
###### [Amazon Link](https://www.amazon.in/gp/product/B00E1GGE40/ref=ppx_yo_dt_b_asin_title_o09_s00?ie=UTF8&psc=1)
##### Adafruit camera extension cable:
###### [Amazon Link](https://www.amazon.in/gp/product/B00XW2NCKS/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)
##### Camera enclosure:
###### [Amazon Link](https://www.amazon.in/gp/product/B00IJZJKK4/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1)
#####    4 channel adjustable IR proximity sensors: 
###### [Amazon Link](https://www.amazon.in/gp/product/B0793NV868/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
##### Short HDMI cable:
###### [Amazon Link](https://www.amazon.in/gp/product/B073VL88C5/ref=ppx_yo_dt_b_asin_title_o06_s00?ie=UTF8&psc=1)
#####    5 inch Touchscreen: 
#####    Jumper wires:
#####    Power Supply:  
#####    27v Water valves: 

## Author:
[Daniel Richardson](github.com/RichardsonDaniel): richardson.daniel@hotmail.co.uk


## License:
 © [Daniel Richardson](github.com/RichardsonDaniel)




