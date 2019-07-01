


 <p align="center">
  <img src="http://richardsondaniel.co.uk/KidsApp/img/english/animals/mouse.png"/>
</p>


#  <p align="center"> Anemotaxis Chamber</p>

<p align="center">"Program to record, time and operate the anemotaxis chamber designed for the lab -  developed for IISER (Indian Institutes of Science Education and Research)"</p>

# 


This program is a basic interface to allow a user to choose between the two underlying programs [PointTracker](https://github.com/RichardsonDaniel/PointTracker) and [ObjectTracker](https://github.com/RichardsonDaniel/ObjectTracker). Both currently under private repos as they are still being developed, major updates will be pushed here.

 -  **PointTracker** is a optical flow solution for tracking mouse muscle movements through pre-recorded videos it includes three distinct modes of tracking; *Multipoint* (base set 1000 points) optical flow upon a scene, *UserPoint* optical flow with user positioning of upto 30 points and *MotionTrack* which tracks the source of motion within the scene and draw its path. These each will output a coordinate (X:Y relating to pixel position) CSV file and a folder containing the post processed frames of the video.

## Files:

[](https://emojipedia.org/file-folder/)
##### - 📁OUTPUT
###### This folder will be uto filled with the CSV sheet with timings/port output file and two video files pers session, on .H264 and one converted .MP4


[](https://emojipedia.org/page-facing-up/)
##### - 📄 FlowCageProgram
###### Python file designed to be run on the raspberry pi in the lab to contol a touchscreen, camera, a set of 8 relays and a bank of IR emmiters/recievers.
[](https://emojipedia.org/page-facing-up/)
##### - 📄 License.txt
###### Liscense is a text file holding the licensing information on the current project, currently  [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html)
[](https://emojipedia.org/page-facing-up/)
##### - 📄 README.txt
###### ReadME is the document you are currently reading holding usage and general information.



### Dependencies: 
The source code on this project is meant to be run on the installed Raspberry Pi on the Anemotaxis chamber, if you require this for your own purpose you will have to repurpose the pin list IN and OUT arrays for your setup, currently pins;

21, 20, 16, 26, 19, 13, 6, 5

are used for outputs to the 8 channel relay, ordered correctly 1 through 8. The pins;

12, 1, 0, 8

are used as input pins from the bank of 4 IR emitters/recievers and are positioned across the 4 flow ports. The rest of the pins (including the 5v power rails) are assigned to the touchscreen.
## Portable Usage:

 1. Load application
 2. Choose trakcer type, Point or Object
 3. Load in your video file, either drag onto terminal window or load from repo (video folder)
 4. Choose your tracker method, Point has three methods and Object has two
 5. Let the tracker run through the video sequence until you choose to stop it or the video ends
 6. The terminal and supporting windows will close when complete
 7. Gather your output CSV and processed frames from the OUTPUT folder. Beware to take out previous test files before running again as these will be overwritten

&nbsp;
<details><summary>Click here for screenshot walkthrough if you wish to use this on your own videos.</summary>
<p>

## Opening menu:

Once the folder is open you will be greeted with the following file structure, to run the overriding application run the .exe in this folder, if you already know which specific kind of tracker you need you can open either ObjectTrackerP or PointTrackerP and run their respective .exe's to skip the main menu sequence. If you are skipping the menu scroll down to the appropriate section for you.

 <p align="center">
  <img src="http://richardsondaniel.co.uk/EggDrop/TrackerScreenshots/1.PNG"/>
</p>
Once you have opened the .exe you will be greeted with this terminal where you can select the kind of tracker you require.
 <p align="center">
  <img src="http://richardsondaniel.co.uk/EggDrop/TrackerScreenshots/2.PNG"/>
</p>
This will then begin a loading sequence for your chosen tracker. Scroll ahead to your appropriate choice.
 <p align="center">
  <img src="http://richardsondaniel.co.uk/EggDrop/TrackerScreenshots/3.PNG"/>
</p>

## POINT TRACKER:
When the load sequence is complete you will be shown a new terminal window, this will read out the videos in the video folder (repo) which you can load by typing; video/name.filetype or if your video file is in an unprotected space you can simply drag it into the terminal and it will create a path itself.
 <p align="center">
  <img src="http://richardsondaniel.co.uk/EggDrop/TrackerScreenshots/point/p1.PNG"/>
</p>
Once a file is chosen you will be asked to choose a tracking type from the three available:

 1. ***MultiPoint;*** this will load a Lucas Kanade optical flow sequence with 1000 points being tracked all these points are chosen by the system on what it deems to be the best for the flow.

</p>
</details>

## Author:
[Daniel Richardson](github.com/RichardsonDaniel): richardson.daniel@hotmail.co.uk


## License:

 [GNU Affero General Public License v3.0](https://www.gnu.org/licenses/agpl-3.0.en.html) © [Daniel Richardson](github.com/RichardsonDaniel)



