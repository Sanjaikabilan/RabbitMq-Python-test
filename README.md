# MQTT-Client-Python-RabbitMQ-Pub/Sub-solution
MQTT Client PUB/SUB using Python and RabbitMQ
 
 
MQTT (formerly the MQ Telemetry Transport) is a lightweight protocol that’s primarily designed for connecting power-constrained devices over low-bandwidth networks. Though it existed for over a decade, the advent of M2M (machine to machine communications) and Internet of Things (IoT) made it a popular protocol.
 
I have created the Messaging queue example using python with MQTT Protocol.
 
Prerequisites:
Python, RabbitMQ due to supports MQTT Protocol and have its own best queue management process.
 
OS platform:
Windows 7 or 10
 
Installation & Dependencies:
Python:
- Download Links: https://www.python.org/downloads/
Download Latest Python from above links and follow the easy steps with run exe files on windows machine.
 
- Pip Installation
There are many methods for getting Pip installed, but my preferred method is the following:
 
Download get-pip.py to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run python get-pip.py. This will install pip.
Verify a successful installation by opening a command prompt window and navigating to your Python installation's script directory (default is C:\Python27\Scripts). Type pip freeze from this location to launch the Python interpreter.
 
pip freeze displays the version number of all modules installed in your Python non-standard library; On a fresh install, pip freeze probably won't have much info to show but we're more interested in any errors that might pop up here than the actual content
Microsoft Windows [Version 6.2.9200]
(c) 2012 Microsoft Corporation. All rights reserved.
 
C:\Users\Username>cd c:\Python27\Scripts
 
c:\Python27\Scripts>pip freeze
 
It would be nice to be able to run Pip from any location without having to constantly reference the full installation path name. If you followed the Python installation instructions above, then you've already got the pip install location (default = C:\Python27\Scripts) in your Windows' PATH ENVIRONMENT VARIABLE. Verify a successful environment variable update by opening a new command prompt window (important!) and typing pip freeze from any location
 
Microsoft Windows [Version 6.2.9200]
(c) 2012 Microsoft Corporation. All rights reserved.
 
C:\Users\Username>pip freeze
 
- Import paho-mqtt to python
From windows command prompt, go to directory c:\Python27\Scripts>.
From Python Script folder run the below command
pip install paho-mqtt
With above Command now we can import paho-mqtt libraries in our python program.
 
RabbitMQ
- Download & Install ERlang first (https://www.erlang.org/)
- Download & Install RabitMQ (http://www.rabbitmq.com/download.html)
- Find Commands Easily
Set up the system path so you can find the server and sbin directory easily.
Create a system environment variable (e.g. RABBITMQ_SERVER) for "C:\Program Files\RabbitMQ\rabbitmq_server-3.7.1". Adjust this if you put rabbitmq_server-3.7.1 elsewhere, or if you upgrade versions.
 
Append the literal string ";%RABBITMQ_SERVER%\sbin" to your system path (aka %PATH%).
Now you can run rabbitmq commands from any (administrator) Command Prompt.
You will need to navigate to rabbitmq_server-3.7.1\sbin to run commands if your system path does not contain the RabbitMQ sbin directory.
 
- Enable MQTT on RabbitMQ: 
Type from windows RUN - %RABBITMQ_SERVER%\sbin and do enter, will open RabbitMQ directory Command Prompt. Type the following command and hit enter, will enable the MQTT on RabbitMQ.
- rabbitmq-plugins.bat enable rabbitmq_mqtt
 
- Enable RabbitMQ Web Interface:
To Enable Web Interface on RabbitMQ, from the above RabbitMQ Command Prompt type and run following command
- rabbitmq-plugins enable rabbitmq_web_mqtt
 
Now we can user http://localhost:15672 url to run web interface in browser, use “guest” keyword as a username and password on login screen, as the default rabbitmq user. For web interface 15672 is the default port.
 
In this web interface you can see the MQTT Client Connections and Subscribed users list.
Also can see the published  message over the topic.
 
Python Programming
mqttClint.py is the python program, open the file in python and run, will subscribe to MQTT and publish a message on topic- test, we can see the output on python prompt with subscribe and publish message details.
