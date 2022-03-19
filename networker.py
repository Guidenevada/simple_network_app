import os
import sys
import time
import json
import socket
import datetime
now = datetime.datetime.now()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def connection(ip):
    for x in range(10):
        try:
            sock.connect((str(ip), 4443))
            break
        except:
            time.sleep(3)
            print("retrying connection")
    
def send(message):
    try:
        sock.send(message.encode())
    except Exception as e :
        os.system("echo '" +e+"' > logs/log"+now.day+ "-" +now.hour+":"+now.minute+","+now.second+".txt")
        print("failed to send message\n\nlogs have been saved in log directory")
        
def main():
    print("hello to my network app")
    

if __name__ == '__main__':
    main()
