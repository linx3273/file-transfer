import socket
import src.funcs as funcs
from tqdm import tqdm

def client():
    SIZE = 1024
    port = 5050
    while True:
        funcs.inpmsg()
        ip = input("Enter IP: ")    

        conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        conn.connect((ip,port))
        data = conn.recv(SIZE).decode()
        funcs.msg()
        print(data)

        if "Accepted" in data:
            funcs.handleConnection(conn)
        
        print()
        funcs.msg()
        print("1. New Connection")
        funcs.msg()
        print("2. Close Client")

        funcs.inpmsg()
        c = int(input("Enter Choice: "))
        if c==1:
            continue
        elif c==2:
            return
        else:
            break