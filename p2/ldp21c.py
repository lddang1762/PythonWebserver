# ldp21c.py
import time
import sys
from socket import *

# UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
serv_addr = ('', 45678)

RTTarr = []
try:
    numPings = int(sys.argv[1])
except IndexError:
    print("\nIncorrect usage. Use: 'python3 ldp21c.py NUM_PINGS' where NUM_PINGS is the desired number of pings.\n")

for x in range(numPings):
    sendTime = time.time()
    message = ('seq ' + str(x+1) + " " + str(time.strftime("%H:%M:%S"))).encode()
    clientSocket.sendto(message, serv_addr)

    try:
        data, server = clientSocket.recvfrom(1024)
        recvTime = time.time()
        rtt = (recvTime - sendTime) * 1000
        RTTarr.append(rtt)
        print("Ping", str(x+1) ,": ", data.decode(), ", RTT =",round(rtt, 4), "ms")

    except timeout:
        print("Ping", str(x+1) ,": ", "Request timed out")

print()
print("--- SUMMARY ---")
print("Minimum RTT: ", round(min(RTTarr), 4), "ms")
print("Maximum RTT: ", round(max(RTTarr), 4), "ms")
print("Average RTT: ", round((sum(RTTarr)/len(RTTarr)), 4), "ms")
print("Number of packets received: ", len(RTTarr))
print("Number of packets lost: ", numPings - len(RTTarr))
print("Packet loss percentage: ", round( ((numPings - len(RTTarr))/numPings*100), 2), "%")
