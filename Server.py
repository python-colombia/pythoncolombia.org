# coding=utf-8
import pickle
import socket
import threading

#vamos a conservar una lista de números.

someList = [1,2,7,9,0]
pickledList = pickle.dumps(someList)

#Nustra Clase hilo

class ClientThread ( threading.Thread ):

	def __init__(self, channel, details):
		
		self.channel = channel
		self.details = details
		threading.Thread.__init__(self)

	def run(self):
		print'Received connection :', self.details[0]
		self.channel.send (pickledList)

		for x in xrange(10):
			print self.channel.recv(1024)
		self.channel.close()
		print 'Closed connection', self.details[0]

# set up the server:

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('',2727))
server.listen(5)

#Have the server serve "Forever":

while True:
   channel, details = server.accept()
   ClientThread ( channel, details ).start()
