import threading
import socket
import sys
import time
import queue as q

print_lock = threading.Lock()

if len(sys.argv) !=2 :
    print ('Usage: python3 portScanner.py <host>')
    sys.exit(1)


host = sys.argv[1]

print ('***** Scanning ' + host + ' *****')

def scan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((host, port))
        with print_lock:
            print('Port: ' + str(port) + ' is open')
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        scan(worker)
        q.task_done()

q = q.Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 65535):
    q.put(worker)

print('***** Scan complete *****')
