#! /usr/bin/env python3

# Python Modules
import time
import numpy as np
import pyaudio as pa 
#import pickle
import pygame
import queue
import socket
import sys
#import os
import threading
import wave
from faster_whisper import WhisperModel

## Ros Modules
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

index = 0
def SaveFile(AudioBuffer: np.ndarray):
    global index
    print(f"[*] len(AudioBuffer): {len(AudioBuffer)}")

    print("[*] Saving file...")
    with wave.open("output" + str(index) + ".wav", "wb") as file:
        file.setnchannels(1)
        file.setsampwidth(2)  # Assuming each sample is 2 bytes (16 bits)
        file.setframerate(44100)
        file.writeframes(AudioBuffer.tobytes())

    index += 1

def SetRobotGoal(goal: str, ID : int) -> (float, float):
    Places = [
        ["sala de estar", (-6.5, 3.0)],
        ["garagem", (-4.9, 3.7)],
        ["quarto A", (-6.4, -1,6)],
        ["quarto B", (6.4, -4.4)],
        ["seção A", (4.8, 1.6)],
        ["seção B", (-3.0, 1.0)],
        ["cozinha", (-2.8, 1.0)],
        ["banheiro", (-1.5, 3.2)]
    ]

    print(f"goal: '{goal}', ID: '{ID}'")
    for i in Places:
        print(f"places.goal: '{i[0]}' places.goal_position: '{i[1]}'")
        if i[0] == goal.replace(" ", ""):
            print("Goal is equal to the list!")
            x = i[1]
            return [x, ID]

    return False


