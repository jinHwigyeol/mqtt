#!/usr/bin/python3
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_connect(client, userdata, flags, rc):
    print ("Connected with rc: " + str(rc)) 
    client.subscribe("home/led", 0)

def on_message(client, userdata, msg):
    #print ("Topic: "+ msg.topic+"\nMessage: "+str(msg.payload)) 
    command = msg.payload.decode() 
    if command == "on":
        print("LED on")
        GPIO.output(4, True)
    elif command == "off":
        print("LED off")
        GPIO.output(4, False)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("203.250.133.24", 1883, 60) # localhost -> IP Address
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

try:
    client.loop_forever()
except KeyboardInterrupt:
    GPIO.cleanup()
