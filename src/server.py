import socket
import src.funcs as funcs

def getIPFromSocket():
    sv  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sv.connect(('8.8.8.8', 80))
    IP,__port = sv.getsockname()
    sv.close()
    return IP

def server():
    # IP = socket.gethostbyname(socket.gethostname()) # gets the ipv4 address automatically and prevent hardcoding the ip address
    # socket.gethostname() => returns the computer name
    IP = getIPFromSocket()
    PORT = 5050
    ADDR = (IP,PORT)
    sv  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sv.bind(ADDR)
    sv.listen()
    funcs.msg()
    print(f"Server is listening on: {IP}")

    while True:
        conn,addr = sv.accept()
        funcs.msg()
        print(f"Request Received from {addr[0]}")
        funcs.msg()
        print("1. Continue")
        funcs.msg()
        print("2. Abort")
        
        funcs.inpmsg()
        c = int(input("Enter choice: "))
        if c==1:        # when accepting the connection
            conn.send("Connection Accepted".encode())
            funcs.handleConnection(conn)
            break              
        elif c==2:      # incase of rejecting the connection
            conn.send("Connection Denied".encode())
            break
        
    sv.close()
    funcs.msg()
    print("Connection Closed")
    


        





