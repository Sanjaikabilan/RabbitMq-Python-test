import paho.mqtt.client as mqtt
import time
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Define callback functions for MQTT events
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("abcd")

def on_message(client, userdata, msg):
    #print(msg.topic + " " + str(msg.payload))
     #print("Received message: " + msg.payload.decode())
     acceleration = float(msg.payload.decode())
     print(acceleration)
     x_data.append(len(x_data))
     y_data.append(acceleration)

# Create an MQTT client object
client = mqtt.Client()

# Set the callback functions for MQTT events
client.on_connect = on_connect
client.on_message = on_message

# Set the username and password for the MQTT client
client.username_pw_set(username="xxjfwlqo:xxjfwlqo", password="9agKXHW-5duIFt7ehaLp6JSM4-L-SMkc")

# Connect to the MQTT broker
client.connect("fly.rmq.cloudamqp.com", 1883, 120)

# Initialize the x and y data lists
x_data = []
y_data = []

# Create a Plotly figure with a scatter plot
fig = make_subplots(rows=1, cols=1)
scatter = go.Scatter(x=x_data, y=y_data, mode="lines")

# Add the scatter plot to the figure
fig.add_trace(scatter)

# Set the plot title and axis labels
fig.update_layout(title="Real-time acceleration data", xaxis_title="Time", yaxis_title="Acceleration (m/s^2)")

# Show the plot
fig.show()


client.publish("ab", "bc")

# Subscribe to a topic
client.subscribe("ab")

# Start the MQTT client loop

client.loop_start()
interval = 100
while True:
    # Update the scatter plot with the new data
    scatter.x = x_data
    scatter.y = y_data
    # Update the x-axis limits to show the most recent data
    fig.update_layout(xaxis=dict(range=[max(0, len(x_data)-100), len(x_data)]))

    # Redraw the plot
    fig.show()
    fig.save("a.png")
    # Wait for the specified interval
    client.loop(timeout=interval/1000.0)

client.loop_stop()





