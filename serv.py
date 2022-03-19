

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



        

def send(message):
    try:
        sock.send(message.encode())
    except Exception as e :
        os.system("echo '" +e+"' > logs/log"+now.day+ "-" +now.hour+":"+now.minute+","+now.second+".txt")
        print("failed to send message\n\nlogs have been saved in log directory")
        
def main():
    print("hello to my network app")
    #ip = input("what is the server ip?")
    ip = '127.0.0.1'
    sock.bind(('', 4448))
    sock.listen(10)

    conn, addr = sock.accept()
    print("connected to " + str(addr))
    conn.send("new connection".encode())
    a = 1
    while (a == 1):
        
        while conn.recv(1024):
            print(conn.recv(1024).decode())
        if conn.recv(1024).decode() == "exit":
            a = 0
            print("connection closed")
            break
        message = input(">")
        conn.send(message)
        if message == "exit":
            a = 0
            
            break
    if a == 0:
        sock.close()
        print("connection closed")
        
if __name__ == '__main__':
    main()
