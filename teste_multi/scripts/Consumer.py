#! /usr/bin/env python3

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
#import wave
from faster_whisper import WhisperModel


class Consumer:
    __AudioQueue = queue.Queue()
    __LengthQueue = queue.Queue(maxsize=2)
    self.__Whisper = None

    def __init__(self):
        self.__Whisper = WhisperModel("base",
                                      device="cpu",
                                      compute_type="int8",
                                      num_workers=10,
                                      cpu_threads=8)
        pass

    def TranscribeBlocking(self, audio_data) -> str:
        audio_data_array: np.ndarray = np.frombuffer(audio_data, np.int16).astype(np.float32) / 255.0

        segments, _ = self.__Whisper.transcribe(audio_data_array,
                                    language="pt",
                                    beam_size=5,
                                    vad_filter=True,
                                    vad_parameters=dict(min_silence_duration_ms=1000))

        segments = [s.text for s in segments]
        transcription = " ".join(segments)
        transcription = transcription.strip()
        print("[*] TranscribeBlocking Executed!")
        return transcription

    def Producer(self):
        while True:
            if True:#self.__RecAudio == True:
                audio_data = b""
                for _ in range(1):
                    chunk = self.__Stream.read(16000)
                    audio_data += chunk
                    pass
                self.__AudioQueue.put(audio_data)
            else:
                pass
            pass
        pass

    def Consumer(self):
        while True:
            if self.__LengthQueue.qsize() >= 2:
                with self.__LengthQueue.mutex:
                    self.__LengthQueue.queue.clear()
                    print()
                    pass
                pass
            if True:
                AudioData = self.__AudioQueue.get()
                self.__LengthQueue.put(AudioData)

                DataToProcess = b""
                for i in range(self.__LengthQueue.qsize()):
                    DataToProcess += self.__LengthQueue.queue[i]
                    pass

                try:
                    Result = self.TranscribeBlocking(DataToProcess)
                    print(f"Result: {Result}")
                except Exception as e:
                    print(f"Error {e}")
                    pass

                self.__AudioQueue.task_done()
                pass
            else:
                #self.__LengthQueue.queue.clear()
                pass
            pass
        pass
    pass


