#!/usr/bin/python3
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))

def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish

mqttc.connect("203.250.133.88", 1883, 60)
mqttc.loop_start()

infot = mqttc.publish("temperature", "25", qos=0)
infot.wait_for_publish()
