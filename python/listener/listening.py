#!/usr/bin/python

from twisted.internet import protocol, reactor

class EchoFactory(protocol.Factory):
	def buildProtocol(self, addr):
		return Echo()

class EchoFactoryAdmin(protocol.Factory):
	def __init__(self,port):
		self.port = port

	def buildProtocol(self, addr):
		return EchoAdmin(self.port)

class Echo(protocol.Protocol):
	def dataReceived(self, data):
		self.transport.write(data)

class EchoAdmin(protocol.Protocol):
	def __init__(self,port):
		self.port = port

	def dataReceived(self, data):
		self.port.write(data)
		self.transport.write(data+"asdfasdfasfd\n")


h=reactor.listenTCP(1234, EchoFactory())
reactor.listenTCP(1235, EchoFactoryAdmin(h))

reactor.run()
