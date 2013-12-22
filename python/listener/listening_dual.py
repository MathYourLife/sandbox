#!/usr/bin/env python

from __future__ import print_function

from twisted.internet import protocol, reactor
from collections import defaultdict

import json

class data(object):

    def __init__(self):
        self.counts = defaultdict(int)

    def update(self, data):
        pass



class dual(object):

    def __init__(self, data_port, admin_port, counts):
        factory = self.EchoFactory()
        factory.counts = counts
        reactor.listenTCP(data_port, factory)

        admin_factory = self.EchoFactoryAdmin()
        admin_factory.counts = counts
        reactor.listenTCP(admin_port, admin_factory)

        reactor.run()

    class Echo(protocol.Protocol):

        def __init__(self, counts):
            self.counts = counts

        def dataReceived(self, data):
            self.counts[data] += 1
            self.transport.write("**%s: %s\n" % (data, self.counts[data]))
            self.transport.write(data)

        def connectionMade(self):
            self.transport.write("Hello basic user.\n")
        def connectionLost(self, reason):
            print("Normal connection lost")

    class EchoFactory(protocol.Factory):

        def buildProtocol(self, addr):
            return dual.Echo(counts=self.counts)
        def clientConnectionFailed(self, connector, reason):
            print("Connection failed - goodbye!")
        def clientConnectionLost(self, connector, reason):
            print("Connection lost - goodbye!")

    class EchoAdmin(protocol.Protocol):

        def __init__(self, counts):
            self.counts = counts

        def dataReceived(self, data):
            self.counts[data] += 1
            self.transport.write("**%s: %s\n" % (data, self.counts[data]))
            self.transport.write(data)

        def connectionMade(self):
            self.transport.write("Welcome admin.\n")
        def connectionLost(self, reason):
            print("admin connection lost")

    class EchoFactoryAdmin(protocol.Factory):
        def buildProtocol(self, addr):
            return dual.EchoAdmin(counts=self.counts)
        def clientConnectionFailed(self, connector, reason):
            print("Admin Connection failed - goodbye!")
        def clientConnectionLost(self, connector, reason):
            print("Admin Connection lost - goodbye!")


# this connects the protocol to a server runing on port 8000
def main():

    with open('config.json') as f:
        config = json.load(f)

    config['counts'] = line_counts
    d=dual(**config)
# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
