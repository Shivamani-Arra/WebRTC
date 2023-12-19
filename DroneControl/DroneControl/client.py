import socket
import time

HOST = "192.168.111.71"
PORT = 5999
def dataTransfer(s,data):

    with open("mydata.txt", "wb") as fo:
        start_time = time.time()
        while data:
            if data.endswith(b"EOF"):
                break
            fo.write(data)
            data = s.recv(1024)

        end_time = time.time()

    print("File closed")
    rtt = end_time - start_time
    print(f"Round-trip time: {rtt} seconds")
    print(f"{(1000 / 1024) / rtt} mbps")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected")
    s.sendall(b"Hello Kiran")
    data = s.recv(1024)
    dataTransfer(s,data)
    while(True):
        data=s.recv()
        if(data.endswith("close")):
            break
        elif(data):
            dataTransfer(s,data)

