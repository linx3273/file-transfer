import socket
import src.funcs as funcs
from tqdm import tqdm

def client():
    SIZE = 1024
    port = 5050
    
    funcs.inpmsg()
    ip = input("Enter IP: ")    

    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    conn.connect((ip,port))
    data = conn.recv(SIZE).decode()
    funcs.msg()
    print(data)

    if "Accepted" in data:
        funcs.handleConnection(conn)
    return