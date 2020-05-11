import paho.mqtt.client as mqtt #import the client1
import time
import matplotlib.pyplot as plt

drawing = []
shape = []
end = False

############
def on_message(client, userdata, message):
    global drawing
    global shape
    global end
    data = str(message.payload.decode("utf-8"))
    if "BEGIN" in data:
        pass
    else:   
        if 'SHAPE' in data or 'PIC' in data:
            print('Shape Added:', shape)
            drawing.append(shape)
            shape = []
        
        shape.append(data)
        print(data)
        if 'END' in data:
            end = True
        
def draw_shape(pointList):
    x = []
    y = []
    for val in pointList:
        if '#' in val:
            color = val
        else:
            if 'SHAPE' in val:
                pass
            else:
                num = val.split(',')
                x.append(float(num[0]))
                y.append(float(num[1]))
    plt.plot(x,y,color)

broker="34.67.109.247"
port=13371

#broker = 'localhost'
#port = 1883

print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.on_message=on_message #attach function to callback
print("connecting to broker")
client.connect(broker,port) #connect to broker
print("Subscribing to topic","eoc/pic")
while end != True:
    client.loop_start()
    client.subscribe("eoc/pic")
    client.loop_stop() #stop the loop

for i in range(len(drawing)):
    if i >0:
        print('shape:',drawing[i])
        draw_shape(drawing[i])

plt.show()
