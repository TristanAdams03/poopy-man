import paho.mqtt.client as mqtt
import matplotlib.pyplot as plt
import time

a = []
b = []
c = []
d = []
e = []
f = []
g = []
h = []
i = []
j = []
k = []
BEND = False
biglist = [a, b, c, d, e, f, g, h, i, j, k]
active = 0

def on_message(client, userdata, message):
    global active
    global biglist
    global end
    
    data = str(message.payload.decode("utf-8"))
    if 'BEGIN' in data:
        pass
    elif 'END' in data:
        BEND = True    
    elif 'SHAPE' in data:
        print("New Shape: ", data)
        active += 1
    else:
        biglist[active].append(data)
    print(data)


# What is this function?
def draw_shape(submitted_shape):
    x = []
    y = []
    for pair in submitted_shape:
        if '#' in pair:
            color = pair
            plt.plot(x,y,color= color)
        elif 'SHAPE' in pair:
            pass
        else:
            x.append(float(pair.split(",")[0]))
            y.append(float(pair.split(",")[1]))

    

broker = "34.67.109.247"
port = 13371

client = mqtt.Client('Sumting')
client.on_message = on_message
client.connect(broker, port)


while BEND != True:
    client.loop_start()
    client.subscribe("eoc/pic")
    client.loop_stop() #stop the loop
print(biglist)
for shape in biglist:
    draw_shape(shape)

plt.show()
