import re
from time import sleep
from serial import Serial
from matplotlib import style
import matplotlib.pyplot as plt
import numpy as np

p = re.compile('h:(\d+)\.\d+\|t:(\d+)\.\d+')

with Serial('/dev/cu.usbmodem143101', 9600) as s:
  fig, graphs = plt.subplots(2)

  fig.suptitle('Temperature and Humidity')

  temp_data = []
  humid_data = []
  plt.ion()
  
  style.use('default')

  while True:
    line = s.readline()
    line = line.decode('utf-8').strip()

    m = p.match(line)

    if m:
      humid, temp = m.groups()

      print('Temperature =', temp)
      temp_data.append(int(temp))
      graphs[0].plot(humid_data, color = '#2d2d30')

      print('Humidity =', humid)
      humid_data.append(int(humid))
      graphs[1].plot(temp_data, color = '#2d2d30')

      plt.draw()
      plt.pause(0.0001)

      sleep(0.01)
