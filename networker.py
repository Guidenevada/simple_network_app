from ast import While
from email import message
import os
from sqlite3 import connect
import sys
import time
import json
import socket
import datetime
now = datetime.datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connection(ip):
    for x in range(5):
        try:
            sock.connect((ip, 4448))
            break

        except:
            time.sleep(3)
            print("retrying connection")
    
def send(message):
    try:
        sock.send(message.encode())
    except Exception as e :
        os.system("echo '" +e+"' > logs/log"+now.day+ "-" +now.hour+":"+now.minute+","+now.second+".txt")
        print("failed to send message\n\nlogs have been saved in log directory\n\n\n"+ e)
        
def main():
    print("hello to my network app")
    #ip = input("what is the server ip?")
    ip = '127.0.0.1'
    #connection(ip)
    sock.connect((ip, 4448))
    #conn, addr = sock.accept()
    #print("connected to " + str(addr))
    sock.send("new connection".encode())
    a = int(1)
    while (a == 1):
        
        while sock.recv(1024):
            print("Recived: "+ sock.recv(1024).decode())
        
        message = input(">")
        sock.send(message.encode())
        if message == "exit":
            a = 0
            
            break
    if a == 0:
        sock.close()
        print("connection closed")
        
if __name__ == '__main__':
    main()
