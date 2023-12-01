#!/bin/bash
rm -f /home/pi/Raspberry/TempSensor/log2.txt
python3 /home/pi/Raspberry/TempSensor/sensor.py >> /home/pi/Raspberry/TempSensor/log2.txt

