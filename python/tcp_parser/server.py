from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


class PostfixLogLineParser(LineReceiver):

    delimiter = b'\n'

    def __init__(self, addr):
        self.addr = addr

    def connectionMade(self):
        print('connection start: %s:%s' % (self.addr.host, self.addr.port))

    def connectionLost(self, reason):
        print('connection ended')

    def lineReceived(self, line):
        print("IN: %s" % line.strip())


class ChatFactory(Factory):

    def __init__(self):
        pass

    def buildProtocol(self, addr):
        return PostfixLogLineParser(addr)


def main():
    reactor.listenTCP(514, ChatFactory())
    reactor.run()


if __name__ == "__main__":
    main()

