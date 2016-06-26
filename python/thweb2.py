
import os
import time
import sys
import Adafruit_DHT as dht
from pubnub import Pubnub

import RPi.GPIO as GPIO ## Import GPIO Library

GPIO.cleanup()

pubnub = Pubnub(publish_key='demo', subscribe_key='demo')
channel = 'pi-house'

pin = 4                         ## We're working with gpio 4
RELAY1 = 21                     ## We're working with gpio 17
RELAY2 = 20                     ## We're working with gpio 27
RELAY3 = 16                     ## We're working with gpio 27
GPIO.setmode(GPIO.BCM)          ## Use BCM pin numbering
GPIO.setup(pin, GPIO.IN)        ## Set gpio 4 to OUTPUT
GPIO.setup(RELAY1, GPIO.OUT)    ## Set gpio 17 to OUTPUT
GPIO.setup(RELAY2, GPIO.OUT)    ## Set gpio 27 to OUTPUT
GPIO.setup(RELAY3, GPIO.OUT)    ## Set gpio 27 to OUTPUT


def _callback(m, channel):
    print 'Hello'
    print(m)
        
    if m['item'] == 'Relay1':
        if m['open'] == True:
            GPIO.output(RELAY1,True)
            print('Relay1 ON')
        else:
            GPIO.output(RELAY1,False)
            print('Relay1 OFF')
		
    if m['item'] == 'Relay2':
        if m['open'] == True:
            GPIO.output(RELAY2,True)
            print('Relay2 ON')
        else:
            GPIO.output(RELAY2,False)
            print('Relay2 OFF')

    if m['item'] == 'Relay3':
        if m['open'] == True:
            GPIO.output(RELAY3,True)
            print('Relay3 ON')
        else:
            GPIO.output(RELAY3,False)
            print('Relay3 OFF')

##def callback(message):
##    print 'Hi'
##    print(message)
            
def _error(m):
	print(m)
 
while True:
    pubnub.subscribe(channels=channel, callback=_callback, error=_error)
    time.sleep(1)               ## Wait 1 second
GPIO.cleanup()                  ## Cleanup


