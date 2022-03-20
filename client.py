
import select
from ast import While
from email import message
import os
from sqlite3 import connect
import sys
import time
import json
import socket
import datetime

#from networker import IP_address
now = datetime.datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)





IP_address = str(input("Enter IP address: "))
#IP_address = '127.0.0.1'
Port = int(4443)
for x in range(20):
    try:
        sock.connect((IP_address, Port))
        break
    except:
        print("Connection failed, retrying...")
        time.sleep(1)
while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, sock]
 
    """ There are two possible input situations. Either the
    user wants to give manual input to send to other people,
    or the server is sending a message to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == sock:
            message = socks.recv(2048)
            print (message.decode())
        else:
            if socks.recv(2048):
                message = socks.recv(2048)
                print (message.decode())
            message = sys.stdin.readline()
            sock.send(message.encode())
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()
sock.close()
