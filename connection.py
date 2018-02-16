#!/usr/bin/env python

# https://docs.python.org/2/library/struct.html
# https://bitcoin.org/en/developer-guide#connecting-to-peers
# https://bitcoin.org/en/developer-reference#version
# https://bitcoin.org/en/developer-reference#protocol-versions
# https://en.bitcoin.it/wiki/Protocol_documentation#Message_structure

import struct
import time
import random
import socket
import sys
import hashlib

if len(sys.argv) <=2:
 print "Usage python connection.py <address> <port>"
 print "Before using it launch wireshark for listening"
 exit()

nbytes = 4096

def funct_bitcoin():

 host = sys.argv[1]
 port = int(sys.argv[2])
 version = struct.pack("i", 70002)
 services = struct.pack("Q", 1)
 timestamp = struct.pack("q", time.time())
 addr_recv_services = struct.pack("Q", 1)
 addr_recv_ip = struct.pack(">16s", "192.168.8.100")
 addr_recv_port = struct.pack(">H", 8333)
 addr_trans_services = struct.pack("Q", 1)
 addr_trans_ip = struct.pack(">16s", "192.168.8.100")
 addr_trans_port = struct.pack(">H", 8333)
 nonce = struct.pack("Q", random.getrandbits(64))
 user_agent_bytes = struct.pack("B", 0)
 starting_height = struct.pack("i", 0)
 relay = struct.pack("?", False)
 payload = version + services + timestamp + addr_recv_services + addr_recv_ip + addr_recv_port + addr_trans_services + addr_trans_ip + addr_trans_port + nonce + user_agent_bytes + starting_height + relay
 magic = "F9BEB4D9".decode("hex")
 command = "version" + 5 * "\00"
 length = struct.pack("i", len(payload))
 check = hashlib.sha256(hashlib.sha256(payload).digest()).digest()[:4]
 msg = magic + command + length + check + payload
 socket_object = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
 socket_object.connect((host,port))
 socket_object.send(msg)
 socket_object.recv(nbytes)

funct_bitcoin()
