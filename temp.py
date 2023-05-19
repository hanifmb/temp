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

        # humidity = sense.get_humidity()
        # temperature = sense.get_temperature()

        humidity = 22
        temperature = 23

        if humidity is not None and temperature is not None:
            sleep(2)

            message = str(temperature)

            topic = "temp"
            client.publish(topic, message)
            
        else:
            print('Failed to get reading. Try again!')	
            sleep(10)

if __name__ == "__main__":
    main()
