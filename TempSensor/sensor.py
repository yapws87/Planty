import Adafruit_DHT
import time
import datetime
import os,sys

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4

#os.remove("log.txt")

while True:
	humidity, temperature = Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
	#ct = datetime.datetime.now()
	ct = time.time()
	with open('/var/www/html/data.csv','a') as datafile:
		if humidity is not None and temperature is not None:
			datafile.write("{} {} {}\n".format(ct,temperature,humidity))
			#datafile.write("{} Temp={}C  Humidty={}% \n".format(ct,temperature,humidity))
	

#if humidity is not None and temperature is not None:
		#print("{:}  Temp={0:0.1f} C  Humidity={1:0.1f} %".format(ct,temperature, humidity))
	#	print("{}  Temp={} C  Humidity={} %".format(ct,temperature, humidity))
	#	sys.stdout.flush()
	#else:
	#	print("Sensor failure")
	time.sleep(60 * 5)
