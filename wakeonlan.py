#!/usr/bin/env python

import socket
import sys

if len(sys.argv) < 3:
    print "Usage: wakeonlan.py [BROADCAST] [MAC]     (example: 192.168.101.255 2F:1E:2D:3C:4B:5A)"
    sys.exit(1)

mac = sys.argv[2]
data = ''.join(['FF' * 6, mac.replace(':', '') * 16])
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(data.decode("hex"), (sys.argv[1], 9))