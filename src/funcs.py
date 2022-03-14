import colorama
from colorama import Fore
from tqdm import tqdm
import os

'''
    module consists of some functions that will be used often in other files
'''


colorama.init(autoreset=True) # autoreset so that the color remains green only for that print line

# when an error has occured
def errmsg():
    print("[" + Fore.RED + "ERR" + Fore.RESET + "]",end=' ')

# when input is required in the current line
def inpmsg():
    print("[" + Fore.YELLOW + "INP" + Fore.RESET + "]",end=' ')

# default info message
def msg():
    print("[" + Fore.GREEN + "INF" + Fore.RESET + "]",end=' ')

# when user provides a option outside the bounds
def invalidChoice():
    errmsg()
    print("Invalid Choice")

# when the client/server is unable to open the file
def openerr():
    errmsg()
    print("Error opening the file. Please check file name")

# when the client/server is unable to send the file
def senderr():
    errmsg()
    print("An error occured while sending the file")

def connerr():
    errmsg()
    print("Unable to connect")


def sendFile(conn):
    SIZE = 1024
    inpmsg()
    filename = input("Enter name of file you want to send: ")
    filesize = os.path.getsize(f"shared/{filename}")
    inf = f"{filename}_{filesize}"

    conn.send(inf.encode())
    bar = tqdm(range(filesize),"Sending: ",unit="B",unit_scale=True,unit_divisor=SIZE)
    with open(f"./shared/{filename}", "rb") as f:
        while True:
            data = f.read(SIZE)

            if not data:
                break

            conn.send(data)

            bar.update(len(data))



def getFile(conn):
    msg()
    print("Waiting to receive a file")
    SIZE = 1024
    data = conn.recv(SIZE).decode()
    data = data.split("_")
    filename,filesize = data[0],int(data[1])
    msg()
    print(f"Receiving a {filename}-[{filesize}Bytes]")

    bar = tqdm(range(filesize),"Receiving: ",unit="B",unit_scale=True,unit_divisor=SIZE)
    
    with open(f"./downloaded/{filename}","wb") as f:
        while True:
            data = conn.recv(SIZE)

            if not data:
                os.system("start .\\downloaded\\")
                break

            f.write(data)
            bar.update(len(data))



def handleConnection(conn):
    while True:
        print()
        msg()
        print("1. Send a file")
        msg()
        print("2. Receive a file")
        msg()
        print("3. Close Connection")
      
        msg()
        c = int(input("Enter Choice: "))
        if c==1:    # when sending a file
            sendFile(conn)                                 
        elif c==2:  # when receiving a file
            getFile(conn)
        elif c==3:  # closing the connection
            return