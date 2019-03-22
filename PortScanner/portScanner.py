import socket #using built in module to access sockets
import sys #for exiting invalid inputs
import ping #user created file for pinging before scanning
from datetime import datetime #for timing

target = raw_input("Enter the DNS to target: ")
check = ping.pingTarget(target)
print(check)
if check != "Success":
    sys.exit()
targetIP = socket.gethostbyname(target)
limit = input("Up to what ports would you like to scan: ") #has to be greater than 1 and less than 65535
if limit < 1 or limit > 65535:
    print("Port number out of range. Exiting")
    sys.exit()

t1 = datetime.now()

try:
    for port in range(1, limit):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket stream
        result = mySocket.connect_ex((targetIP, port))
        if result == 0:
            print ("Port {}:      Open".format(port))
        mySocket.close()

except socket.gaierror:
    print ("DNS could not be resolved. Exiting")
    sys.exit()

except socket.error:
    print ("Failed connection to server")
    sys.exit()

t2 = datetime.now()

timeElapsed = t2 - t1

print "\nScanning completed in: ", timeElapsed
