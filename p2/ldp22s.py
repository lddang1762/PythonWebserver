# ldp22s.py
import time
import sys
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# timeout after 10 seconds
serverSocket.settimeout(10)
# Assign IP address and port number to socket
serverSocket.bind(('', 45678))

interval = 0

while True:
    prevTime = time.time()
    try:
        message, address = serverSocket.recvfrom(1024)
        recvTime = time.time()
        interval = recvTime - prevTime
        print("Server received " + message.decode() + ". Pulse interval was "  + str(round(interval, 1)) + " seconds.")

    except timeout:
        print("No pulse after 10 seconds. Server quits.\nServer stops.")
        serverSocket.close()
        sys.exit()
