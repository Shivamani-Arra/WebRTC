import socket
import time
HOST="172.168.5.11"
PORT=65432
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
   
    s.connect((HOST,PORT))
    print("connected")
    s.sendall(b"Hello Kiran")
    with open("mydata.txt", "wb") as fo:
        start_time = time.time()
        data = s.recv(1024)
        while data:
            if(data==b"-1"):
                break
            fo.write(data)
            data = s.recv(1024)

        end_time = time.time()
    print("file closed")
rtt = end_time - start_time
print(f"Round-trip time: {rtt} seconds")
print(f"{1/rtt} mbps")
# print(f"Recieved from server {data}")

