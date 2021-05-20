# ldp22c.py
import time
import sys
from socket import *

# UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
serv_addr = ('', 45678)

RTTarr = []
try:
    numPings = int(sys.argv[1])
except IndexError:
    print("\nIncorrect usage. Use: 'python3 ldp22c.py NUM_PINGS' where NUM_PINGS is the desired number of pings.\n")

for x in range(numPings):
    message = ("heartbeat pulse " + str(x+1)).encode()
    clientSocket.sendto(message, serv_addr)
    print(message.decode())
    time.sleep(5)
