import socket
import time
HOST="192.168.124.160"
PORT=65432
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr=s.accept()
    print("connection established")
    # with conn:
    #     print(f"Connected by {addr}")
    while True:
        data=conn.recv(1024)
        print(f"Recieved from client {data}")
        start_time = time.time()
        with open("data.txt", "rb") as fi:
            data = fi.read(1024)
            while data:
                conn.send(data)
                data = fi.read(1024)
        conn.send(b"EOF")
        end_time = time.time()
        print("File sent successfully")
        rtt = end_time - start_time
        print(f"Round-trip time: {rtt} seconds")
        print(f"{(1000/1024)/rtt} mbps")