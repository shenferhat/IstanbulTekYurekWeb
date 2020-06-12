import os
import time
from random import randint

print "Simulasyon basliyor"

# sol ust 41.285876, 28.686255
# sol alt 40.981155, 28.652982
# sag ust 41.193491, 29.448951
# sag alt 40.891663, 29.251068

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def randomLat():
    range_start = 25000
    range_end = 150000
    return randint(range_start, range_end)

def randomLon():
    range_start = 25000
    range_end = 300000
    return randint(range_start, range_end)

try:
  while True:
    lat = randomLat()
    lon = randomLon()
    os.system("mosquitto_pub -h test.mosquitto.org  -t 'isttest/devices' -m '{\"lat\": 41."+str(lat).zfill(6) +",\"lon\": 29."+str(lon).zfill(6) +",\"tst\": 1569988874}' ")
  #  lat += 1000;
    time.sleep(.500)
except KeyboardInterrupt:
  print('Durduruldu!')