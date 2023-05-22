# from sense_hat import SenseHat
from time import sleep
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to the MQTT broker")
    else:
        print("Connection failed")

def on_disconnect(client, userdata, rc):
    print("Disconnected from the MQTT broker")

def main():

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    broker_address = "localhost"
    port = 1883

    client.connect(broker_address, port)

    # sense_hat 
    # sense = SenseHat()

    while(True):

        # humidity = str(sense.get_humidity())
        # temperature = str(sense.get_temperature())

        temperature = str(23.333)
        humidity = str(22.222)

        if humidity is not None and temperature is not None:
            sleep(1)

            topic1 = "temp"
            topic2 = "humidity"

            client.publish(topic1, temperature)
            client.publish(topic2, humidity)
            
        else:
            print('Failed to get reading. Try again!')	
            sleep(1)

if __name__ == "__main__": main()
