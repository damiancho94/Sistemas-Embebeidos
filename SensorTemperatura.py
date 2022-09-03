from time import sleep, strftime, time

from w1thermsensor import W1ThermSensor

import csv
import datetime

from datetime import datetime
import os

csv_file = str(datetime.now().strftime('%Y_%m_%d')) +'_TEMPERATURA' + '.csv'

sensor = W1ThermSensor()

with open(csv_file, "a") as log:
	
	while True:
		temperatura = sensor.get_temperature()
		print("the temperature is %s Celsius" % temperatura)
		log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temperatura)))	
		sleep(1)
		
print(output)
