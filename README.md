## This project depends on:
- ros noetic running on ubuntu 20.04: https://wiki.ros.org/noetic/Installation
- move_base: https://wiki.ros.org/move_base

comandos:

    sudo apt install ros-noetic-move-base
   
- multi-robot-rrt-exploration-noetic project: https://github.com/hikashi/multi-robot-rrt-exploration-noetic and its dependencies
- faster_whisper: https://github.com/SYSTRAN/faster-whisper.

commandos:

    sudo apt install python3-pip
    pip install faster-whisper


## Install Commands:
Installing the earlier projects and its dependencies, you'll also need to install these, this should be enough to make the code run properly.
    
    sudo apt install python3-pyaudio
    sudo apt install python3-pygame

## Running:
To Run you'll need to set client.py as executable (Run this on the scripts folder):

    chmod u+x Client.py 
and then run the code with:

    rosrun teste_multi Client.py

! You'll also need to choose a turtlebot3 model before running. !
