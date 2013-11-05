#!/usr/bin/python

import sys
import time
import random
import json


end_time = time.time() + 120

def z():

    n = 0
    for _ in xrange(10):
        n += random.random()
    n /= 10
    n -= 0.5
    return n


while time.time() < end_time:
    time.sleep(0.1)

    if time.time() % 30 < 15:
        v = 4.0
    else:
        v = -4.0

    data = (v + z(), v + z())
    sys.stdout.write("%s\n" % json.dumps(data))
    sys.stdout.flush()

