ear/usr/bin/env python3

#import pickle
#import pyaudio as pa
#import socket
#import struct
#import wave
#import json
#import whisper
#from ctransformers import AutoModelForCausalLM

import sys

import Core

if __name__ == "__main__":
    Portn : int = None
    CoreServer : Core.CoreServer = None 
    if(len(sys.argv)) != 2:
        Portn = int(input("Port Number: "))
        CoreServer = Core.CoreServer(Address="127.0.0.1", Port=Portn)

    elif len(sys,argv) == 2:
        CoreServer = Core.CoreServer(Address="127.0.0.1", Port=int(s.argv[1]))

    print("Creating Main Thread...")
    CoreServer.Main()
