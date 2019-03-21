#MUST BE ROOT - pyping creates raw packets under the hood that requires root access

import pyping

def pingTarget(x):
    #target = raw_input("Enter the DNS of the target: ")

    response = pyping.ping(x)

    if response.ret_code == 0:
        return "Success"
    else:
        return "Failed with {}".format(response.ret_code)
