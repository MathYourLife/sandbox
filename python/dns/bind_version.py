#!/usr/bin/python
from socket import *
import binascii, string, sys
#import pdb; pdb.set_trace()

print '[*]ISC BIND DNS Version Detection'
print '[*]Coded by Sujit Ghosal'
print '[*]Mail: x13.x37@gmail.com'
print '[*]Copyright: WikiSecure Blogs'
print '[*]All rights reserved\n'

host = raw_input('[*]Enter Target Host IP Address/Hostname: ')
port = 53
buffer = 1024
loc = (host, port)

# Creating UDP socket object
sockUDPObj = socket(AF_INET, SOCK_DGRAM)

# DNS Protocol Version Query Request
verPayload   = '\x02\xec'     # Transaction ID
verPayload  += '\x01\x00'     # Standard query flag
verPayload  += '\x00\x01'     # Questions
verPayload  += '\x00\x00'     # Number of Answers
verPayload  += '\x00\x00'     # Number of Authoritative Records
verPayload  += '\x00\x00'     # Number of Additional Records
verPayload  += '\x07\x76\x65\x72\x73\x69\x6f\x6e\x04\x62\x69\x6e\x64\x00\x00\x10\x00\x03'    # version.bind Request

while(1):
    if not verPayload:
        print '[*] No DNS Query sent to the target', host
        break
    else:
        try:
            if(sockUDPObj.sendto(verPayload, loc)):
                response = sockUDPObj.recv(1024, 0)
                sockUDPObj.close()
                if not response:
                    sys.exit(0)
                    print '[*]Error receiving DNS Response. Quiting.'
                    break
                else:
                    print '[*]DNS Response Received.'
                    hexRes = repr(response)
                    break
        except Exception, msg:
            print 'Something went wrong'
            break

sockUDPObj.close()
print response
x = 0
for i in response:
    if (i == '\xc0'):
        x = x+ 9
        length1 = binascii.hexlify(response[x+1:x+3])
        length = string.atoi(length1, 16)
        array_bytes = response[x+3:x+3+length]
        break
    x = x+1

print '[*]Target Host DNS Version: ' + array_bytes,


