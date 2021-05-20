#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket

# TASK 1
#Fill in start
serverSocket.bind(('localhost', 45678))
serverSocket.listen()
#Fill in end

while True:
   #Establish the connection
   print('Ready to serve...')

   # TASK 2
   connectionSocket, addr = serverSocket.accept() #Fill in start  #Fill in end

   try:

      # TASK 3
      message = connectionSocket.recv(1024) #Fill in start      #Fill in end

      filename = message.split()[1]
      f = open(filename[1:])

      # TASK 4
      outputdata = f.read() #Fill in start       #Fill in end

      # TASK 5
      #Send one HTTP header line into socket
      #Fill in start
      header = 'HTTP/1.1 200 OK\r\n'      
      connectionSocket.send(header.encode('utf-8'))
      #Fill in end

      #Send the content of the requested file to the client
      for i in range(0, len(outputdata)):
         connectionSocket.send(outputdata[i].encode('utf-8'))
      connectionSocket.send("\r\n".encode('utf-8'))
      connectionSocket.close()
   except IOError:
      # TASK 6
      #Send response message for file not found
      #Fill in start
      notFound = 'HTTP/1.1 404 Not Found\r\n'
      connectionSocket.send(notFound.encode('utf-8'))
      #Fill in end

      # TASK 7
      #Close client socket
      #Fill in start
      connectionSocket.close()
      #Fill in end

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
