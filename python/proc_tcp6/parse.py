#!/usr/bin/python
"""
Based on tcp4 work here http://voorloopnul.com/blog/a-python-netstat-in-less-than-100-lines-of-code/
"""

from __future__ import print_function

def _hex2dec(s):
    return str(int(s,16))


def _ip(s):
    ip = [(_hex2dec(s[6:8])),(_hex2dec(s[4:6])),(_hex2dec(s[2:4])),(_hex2dec(s[0:2]))]
    return '.'.join(ip)


def split_by_n(seq, n):
    """A generator to divide a sequence into chunks of n units."""
    while seq:
        yield seq[:n]
        seq = seq[n:]


def _convert_ip_port(ipport):
    host,port = ipport.split(':')

    port_dec = _hex2dec(port)

    print(ipport)
    print(host)

    ipv6 = ''
    for group in xrange(4):
        for octet in xrange(4,0,-1):

            left = group * 8 + (octet-1) * 2
            right = group * 8 + octet * 2
            print (left, right)
            ipv6 += host[left: right]

    print(port_dec)
    print(ipv6)
    print(':'.join(split_by_n(ipv6, 4)))


def run():
    with open('/proc/net/tcp6') as f:
        line = f.readline()
        while True:
            line = f.readline()
            if not line:
                break
            parts = line.strip().split(' ')
            _convert_ip_port(parts[2])

_convert_ip_port('0000000000000000FFFF00008AF90DCC:01BB')

print(_ip('CC0DF98A'))
print(_ip('8AF90DCC'))


