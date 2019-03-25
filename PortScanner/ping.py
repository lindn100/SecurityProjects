import os

def pingTarget(x):

    response = os.system("ping -c 1 " + x + ">/dev/null")

    if response == 0:
        return "Success"
    else:
        return "Failed with {}".format(response)
