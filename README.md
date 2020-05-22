# PiSmartlet
---
### The Idea
* https://docs.google.com/presentation/u/2/d/1d2CM4F7Oz5xv9OIyyUduo07Rzwog_qqWEJhAlCR8phg/edit?usp=sharing

## Three parts
---

## The frontend

* Problem: User needs to be able to schedule their device to turn on.
* Solution build an app using ionic to interface with a backend written in Flask to schedule events
  * Step 1: Prototype using figma \
![alt text](https://github.com/the-dev-bin/PiLet/blob/master/pics/prototype.png "Logo Title Text 1")


  * Step 2: Identify framework
    * Used ionic for the easy capability to transfer to an android app in the future
  * Step 3: Build the thing!
  * Step 4: Revel in the glory of site being done 
  
![alt text](  https://github.com/the-dev-bin/PiLet/blob/master/pics/finishedproduct.png "Finished thing!")
  
   
## The Backend
* Problem: Interface between User application and PI.
* Solution: Using flask create an API to handle user data with PI data.
*  Created endpoints on cloud server and used nosql via a single json file to manage user start and end times.

## The Pi
* Problem: Pi must control outdoor outlet via statebased relay.
* Solution: Using a Songle SRD-05VDC-SL-C and a Raspberry Pi Zero W. Utilizing python with RpI.GPIO library and the 5v GPIO signal pins from the PIZero create an IoT outlet that can be controlled by the PI.
* Large amount of hardware work required to safely implement the PI for outdoors.
* See Slideshow for a more indetail aproach on how it was physically built.

## The Parts List And Guide
* Comming Soon™
* https://docs.google.com/presentation/u/2/d/1d2CM4F7Oz5xv9OIyyUduo07Rzwog_qqWEJhAlCR8phg/edit?usp=sharing
