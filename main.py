import server
import client
import message

if __name__=="__main__":
    flag = True
    while(flag):
        print()
        message.msg()
        print("1. Host")
        message.msg()
        print("2. Connect to a host")
        message.msg()
        print("3. Exit")
        try:
            message.inpmsg()
            c = int(input("Enter Choice: "))
            if(c==1):       # Acting as server
                server.server()
            elif(c==2):     # Acting as Client
                client.client()
            elif(c==3):
                message.msg()
                print("Exiting Program...")
                flag = False    # to terminate the program by invalidating the pass case for the loop
            else:
                raise ValueError()
        except:
            message.errmsg()
            print("Invalid Choice. Try Again")
    
        
