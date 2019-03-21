import socket #using built in module to access sockets
import sys #for exiting invalid inputs
import ping #user created file for pinging before scanning
from datetime import datetime #for timing

target = raw_input("Enter the DNS to target: ")
check = ping.pingTarget(target)
if check != "Success":
    print(check)
    sys.exit()
targetIP = socket.gethostbyname(target)
limit = raw_input("Up to what ports would you like to scan: ") #has to be greater than 1 and less than 65535
if limit < 1 || limit > 65535:
    limit = raw_input("Port number out of range. Exiting")
    sys.exit()

t1 = datetime.now()

try:
    for port in range(1, limit):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creating a socket stream
        result = sock.connect_ex(remoteServerIP, port)
        if result == 0:
            print "Port {}:      Open".format(port)
        sock.close()

except socket.gaierror:
    print "DNS could not be resolved. Exiting"
    sys.exit()

except socket.error:
    print "Failed connection to server"
    sys.exit()

t2 = datetime.now()

print "\nScanning completed in: ", t2-t1
