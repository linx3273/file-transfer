import colorama
from colorama import Fore

'''
    consists of the color coded info messages to classify the kind of messages given by the program
    classified into 3 kinds
    MSG - any kind of message provided by the server
    INP - when user input is required
    ERR - when a error occurs
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
    print("[" + Fore.GREEN + "MSG" + Fore.RESET + "]",end=' ')