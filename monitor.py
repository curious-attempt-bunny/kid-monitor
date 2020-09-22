#!/bin/env python3

import schedule
import time
import datetime
import os

def screen_capture():
  timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
  os.system('screencapture -t jpg -x -C screencaptures/{}.jpg'.format(timestamp))
  os.system('curl -X POST http://192.168.0.38:5000/image -F "image=@screencaptures/{}.jpg"'.format(timestamp))
schedule.every(30).seconds.do(screen_capture)

screen_capture()
while True:
  schedule.run_pending()
  time.sleep(1)