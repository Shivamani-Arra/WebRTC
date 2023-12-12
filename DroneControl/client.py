import socket
import time

HOST = "172.168.0.46"
PORT = 5999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Connected")
    s.sendall(b"Hello Kiran")

    with open("mydata.txt", "wb") as fo:
        start_time = time.time()
        data = s.recv(1024)
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
