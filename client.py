from socket import *
import struct
import time
import datetime

host = 'localhost'
port = 123

sock = socket(AF_INET, SOCK_DGRAM)
sock.sendto(b'',(host, port))
data = sock.recvfrom(1024)
timestamp = struct.unpack(">q",data[0])[0]
localtime = time.localtime(timestamp)
print(time.localtime())
print('year: ' + str(localtime.tm_year))
print('month: ' + str(localtime.tm_mon))
print('days: ' + str(localtime.tm_mday))
print('hours: ' + str(localtime.tm_hour))
print('mins: ' + str(localtime.tm_min))
print('secs: ' + str(localtime.tm_sec))