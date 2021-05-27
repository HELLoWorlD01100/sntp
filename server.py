from socket import *
import time
import struct

host = 'localhost'
port = 123
conn = socket(AF_INET, SOCK_DGRAM)
conn.bind((host, port))

def start(shift):
    print("Сдвиг = ", shift, " секунд")
    while True:
      request = conn.recvfrom(1024)
      conn.sendto(struct.pack(">q",int(time.time()+shift)), request[1])

if __name__ == '__main__':
    with open('config.txt') as f:
        shift = f.readline()
        start(int(shift))
    

      
      
