import socket
import time
import datetime
import sys


host = '127.0.0.1'
port = 5001

client_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ping = "ping"

print(f"date of sending request by client is {datetime.datetime.now()}")
start_time = time.time()
client_socket.send(ping.encode())
date = client_socket.recv(1024).decode()
recv_time = time.time()
time_taken = recv_time-start_time

print(f"time taken is {time_taken}s")
print(f"date on server:{date}")
client_socket.close()
