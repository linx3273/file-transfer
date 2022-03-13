import src.server as server
import src.client as client
import src.funcs as funcs
import os

def runner():
    try:
        os.mkdir("shared")
        os.mkdir( "downloaded")
    except: # incase the folders already exist
        pass    

    while True:
        print()
        funcs.msg()
        print("1. Host")
        funcs.msg()
        print("2. Connect to a host")
        funcs.msg()
        print("3. Exit")

        funcs.inpmsg()
        c = int(input("Enter Choice: "))
        print()
        if c==1:       # Acting as server
            server.server()
        elif c==2:     # Acting as Client
            client.client()
        elif c==3:
            funcs.msg()
            print("Program Closed")
            break;  # stopping program by breaking the loop
