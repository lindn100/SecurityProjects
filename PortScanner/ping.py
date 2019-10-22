import sys
import os

if len(sys.argv) !=2:
	print ('Usage: python3 ping.py <host>')
	sys.exit(1)

host = sys.argv[1]

print ('***** Pinging ' + host + ' *****')


def pingTarget(x):
    response = os.system('ping -c 1 -i 0.2 ' + x + '>/dev/null') #ping 1 packet with a 0.2s timeout

    if response == 0:
        print ('Success')
    else:
        print ('Failed with {}'.format(response))

pingTarget(host)
