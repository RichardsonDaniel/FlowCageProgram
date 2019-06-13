#!/usr/bin/python
import RPi.GPIO as GPIO
from gpiozero import CPUTemperature
import time
import picamera
import csv
import random
import webbrowser
from time import strftime
from subprocess import call
from appJar import * 
 

# Variables and setup
GPIO.setmode(GPIO.BCM)
SleepTimeS = 0.1
pinList = [21, 20, 16, 26, 19, 13, 6, 5]
pinListIN = [12, 1, 0, 8]
portList = [] 
camera = picamera.PiCamera()
#camera.resolution = (1280, 720)

# Initialize GPIO pins and default them
for i in pinListIN: 
    GPIO.setup(i, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    
for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)
    
# Define the main program to be run
def beginTrial():
    #Get Variables form GUI
    mouse = program.getEntry("Mouse Number")
    portNum = program.getOptionBox("How many ports in use")
    portCorrectNum = int(program.getOptionBox("Which port is correct?"))
    firingTime = float(program.getOptionBox("How long should the valve fire for (S)?"))

    #Begin timer and write beginning variables to sheet
    start = time.time()
    startDisplay = strftime("%H-%M-%S")
    CSV.writerow(["Mouse Number", mouse])
    CSV.writerow(["Num of ports used", portNum])
    CSV.writerow(["Correct Port", portCorrectNum])
    CSV.writerow(["START TIME", startDisplay])
    CSV.writerow(["------", "------"])

    #Start recording and create file names for conversion later
    camera.start_recording("/home/pi/Desktop/FlowCageProgram/OUTPUT/Mouse_" + mouse + "-"+ startDisplay + '.h264')
    fileName = "Mouse_" + mouse + "-"+ startDisplay + '.h264'
    fileNameMP4 = "Mouse_" + mouse + "-"+ startDisplay + '.mp4'
    print(fileName)

    #Continous loop until correct port (portCorrectNum) shows tripped
    
    while GPIO.input(pinListIN[portCorrectNum-1]) == True:
        if GPIO.input(pinListIN[0]) == False:
            CSV.writerow(["PORT 1 TRIPPED", strftime("%H:%M:%S")])
            print("PORT 1 TRIPPED")
        if GPIO.input(pinListIN[1]) == False:
            CSV.writerow(["PORT 2 TRIPPED", strftime("%H:%M:%S")])
            print("PORT 2 TRIPPED")
        if GPIO.input(pinListIN[2]) == False:
            CSV.writerow(["PORT 3 TRIPPED", strftime("%H:%M:%S")])
            print("PORT 3 TRIPPED")
        if GPIO.input(pinListIN[3]) == False:
            CSV.writerow(["PORT 4 TRIPPED", strftime("%H:%M:%S")])
            print("PORT 4 TRIPPED")
        time.sleep(0.1);

    #End timer and fire off correct pin for water deliver
    end = time.time()
    endDisplay = strftime("%H:%M:%S")
    GPIO.output(pinList[portCorrectNum-1], GPIO.LOW)
    time.sleep(firingTime)
    GPIO.output(pinList[portCorrectNum-1], GPIO.HIGH)

    #Stop recording and write end variables to sheet
    CSV.writerow(["correct port tripped"])
    CSV.writerow(["------", "------"])
    CSV.writerow(["END TIME", endDisplay])
    camera.stop_recording()
    TotalTime = end - start
    program.setLabel("question", "Time Taken: " + str(TotalTime))
    CSV.writerow(["TOTAL TIME", str(TotalTime)])
    CSV.writerow(["   ", "   "])

    #Navigate to output folder and convert .h264 video to .mp4
    directory = "/home/pi/Desktop/FlowCageProgram/OUTPUT/"
    command = "MP4Box -add " + fileName + " " + fileNameMP4
    print(command)
    #subprocess.check_call([command], cwd=directory)
    call([command], shell=True, cwd=directory)
    program.setMessage("output", "Done")
    print("vid converted")
    
# Open an excel file and begin GUI sequence
fileTime = strftime("%H-%M-%S")
with open("/home/pi/Desktop/FlowCageProgram/OUTPUT/FCP - " + fileTime + '.csv', "w") as csvFile:
    CSV = csv.writer(csvFile)

    # Inputs for buttons pressed on GUI
    def ButtonHandler(select):  # Called when user clicks button

        if select == "Begin":  # If user clicks 'Begin'
            if program.getRadioButton("option") == "Start a standard trail":  # If user had chosen 'Start a standard trail'
                beginTrial()

            else:  # If user had chosen 'Test IR emitters to relay/valve connection'
                i= 0
                while i < 100:
                    GPIO.output(21, GPIO.input(12))
                    GPIO.output(20, GPIO.input(1))
                    GPIO.output(16, GPIO.input(0))
                    GPIO.output(26, GPIO.input(8))
                    i += 1
                    time.sleep(0.1);
        elif select == "Test LED":  # If user clicks 'Test LED'
            for i in pinList:
                GPIO.output(i, GPIO.LOW)
                time.sleep(0.5);
                GPIO.output(i, GPIO.HIGH)
                
            for i in pinList:
                GPIO.output(i, GPIO.LOW)
                time.sleep(SleepTimeS);
            for i in pinList:
                GPIO.output(i, GPIO.HIGH)
                time.sleep(SleepTimeS);
            pinList.reverse()
            for i in pinList:
                GPIO.output(i, GPIO.LOW)
                time.sleep(SleepTimeS);
            for i in pinList:
                GPIO.output(i, GPIO.HIGH)
                time.sleep(SleepTimeS);
            pinList.reverse()
                
        elif select == "Test Cam":  # If user clicks 'Test Cam'
            camera.start_preview()
            time.sleep(5)
            camera.stop_preview()
            
        elif select == "Flip Cam":  # If user clicks 'Flip Cam'
            if camera.vflip == False:
                camera.vflip = True
                isCamflipped = True
                print ("Cam Flip True")
            else:
                camera.vflip = False
                isCamflipped = False
                print ("Cam Flip False")
            
        elif select == "Get Num List":  # If user clicks 'Get Num List'
            numberOfPorts = program.integerBox("Number needed", "How many ports, of each kind do you need in list?")
            portNum = program.getOptionBox("How many ports in use")
            portList = []
            
            if portNum == "1":
                portList.insert(1, "If only one port is in use there is no need for a list :)")
                
            if portNum == "2":
                j = 0
                while j < numberOfPorts:
                    portList.insert(1, 1)
                    portList.insert(1, 2)
                    j += 1
            
            if portNum == "3":
                j = 0
                while j < numberOfPorts:
                    portList.insert(1, 1)
                    portList.insert(1, 2)   
                    portList.insert(1, 3)
                    j += 1                 
            
            if portNum == "4":
                j = 0
                while j < numberOfPorts:
                    portList.insert(1, 1)
                    portList.insert(1, 2)
                    portList.insert(1, 3)
                    portList.insert(1, 4)
                    j += 1
        
            random.shuffle(portList)
            random.shuffle(portList)
            random.shuffle(portList)
            outputList = ""
            print(len(portList))
            for i in range(0, len(portList)):
                outputList = outputList + " "
                outputList = outputList + str(portList[i])
            program.infoBox("List", "Shuffled list: " + outputList)
            print(outputList)
        
     
        elif select == "Save & Exit":  # If user clicks 'Save & Exit'
            csvFile.close() # Close file
            GPIO.cleanup() # Cleanup pins
            #webbrowser.open("/home/pi/Desktop/FlowCageProgram/OUTPUT")
            quit()  # Close program
     
    #~~~~~~~~~~~~~~~~~~

    # Create GUI
    program = gui("Flow Cage Program (FCP)", "500x400")  # Sets size and title of main GUI
    program.setBg("lightBlue")  # Sets background colour
     
    # Label and Option boxes within GUI
    program.addLabel("welcome", "Welcome! to Big E's flow program")  # Title
    program.setLabelBg("welcome", "light gray")  # Sets title background
    program.addLabelEntry("Mouse Number")
    program.addLabelOptionBox("How many ports in use", ["1", "2", "3","4"])
    program.addLabelOptionBox("Which port is correct?", ["1", "2", "3","4"])
    program.addLabelOptionBox("How long should the valve fire for (S)?", ["0.5", "0.25", "1","2"])
    program.addLabel("question", "What would you like to do?")  # Label
     
    # Radiobuttons within GUI
    program.addRadioButton("option", "Start a standard trail")
    program.addRadioButton("option", "Test IR emitters to relay/valve connection for 10s")
    
    program.addEmptyMessage("output")
     
    # Buttons within GUI
    program.addHorizontalSeparator(colour="blue")
    program.addButtons(["Begin", "Get Num List", "Flip Cam"], ButtonHandler)
    program.addButtons(["Test Cam", "Test LED", "Save & Exit"], ButtonHandler)
         
    # Start GUI
    program.go()